import { describe, expect, it } from 'vitest';
import { lessonDeadline, mergeFeedback, parseTutorEvent, secondsRemaining, type TutorFeedback } from '../tutor-events';

const encode = (value: unknown) => new TextEncoder().encode(JSON.stringify(value));
const feedback: TutorFeedback = {
  version: 1, turn_id: 'turn-1', original: 'Maine customer calls handle kiye.',
  corrected: 'I handled customer calls.', explanation: 'Use the past tense for previous work.',
  action: 'correct', spoken_response: 'Try saying: I handled customer calls.',
};

describe('tutor room packets', () => {
  it('preserves mixed language original and a separate correction', () => {
    const event = parseTutorEvent(encode(feedback), 'tutor.feedback');
    expect(event).toEqual({ topic: 'tutor.feedback', data: feedback });
    expect(feedback.original).toBe('Maine customer calls handle kiye.');
  });
  it('rejects corrupt data, unsupported versions, missing originals and invalid action types', () => {
    for (const data of [null, {}, { ...feedback, version: 2 }, { ...feedback, original: undefined },
      { ...feedback, action: 'replace-transcript' }, { ...feedback, action: ['continue'] }, { ...feedback, corrected: null },
      { ...feedback, explanation: 42 }, { ...feedback, original: 'x'.repeat(20_001) }]) {
      expect(parseTutorEvent(encode(data), 'tutor.feedback')).toBeNull();
    }
    expect(parseTutorEvent(new Uint8Array([255]), 'tutor.feedback')).toBeNull();
    expect(parseTutorEvent(encode(feedback), 'other.topic')).toBeNull();
  });
  it('accepts assistance feedback without treating it as a new correction', () => {
    const assistance: TutorFeedback = {
      ...feedback,
      turn_id: 'turn-help',
      original: 'Please explain that in Hindi',
      action: 'assist',
      explanation: 'भूतकाल के लिए इस क्रिया का इस्तेमाल करते हैं।',
      spoken_response: 'भूतकाल के लिए इस क्रिया का इस्तेमाल करते हैं।',
    };
    expect(parseTutorEvent(encode(assistance), 'tutor.feedback')).toEqual({
      topic: 'tutor.feedback',
      data: assistance,
    });
  });
  it('allows clarification without fabricating a correction', () => {
    const data = { ...feedback, corrected: null, explanation: null, action: 'clarify' };
    expect(parseTutorEvent(encode(data), 'tutor.feedback')?.data).toEqual(data);
  });
  it('validates lesson deadline and provider failure messages', () => {
    expect(parseTutorEvent(encode({ version: 1, state: 'started', deadline_ms: 1234 }), 'tutor.lesson')).not.toBeNull();
    expect(parseTutorEvent(encode({ version: 1, state: 'started', deadline_ms: 'later' }), 'tutor.lesson')).toBeNull();
    expect(parseTutorEvent(encode({ version: 1, message: 'Speech service is unavailable.' }), 'tutor.error')?.topic).toBe('tutor.error');
    const recoverable = parseTutorEvent(encode({ version: 1, message: 'Retry later.', recoverable: true }), 'tutor.error');
    expect(recoverable).toEqual({ topic: 'tutor.error', data: { version: 1, message: 'Retry later.', recoverable: true } });
    expect(parseTutorEvent(encode({ version: 1, message: 'Invalid.', recoverable: 'yes' }), 'tutor.error')).toBeNull();
  });
});

describe('lesson lifecycle', () => {
  it('cannot extend the local ten-minute cap or show negative remaining time', () => {
    expect(lessonDeadline(600_000, 900_000)).toBe(600_000);
    expect(lessonDeadline(600_000, 300_000)).toBe(300_000);
    expect(secondsRemaining(600_000, 0)).toBe(600);
    expect(secondsRemaining(600_000, 600_001)).toBe(0);
  });
  it('deduplicates retransmitted feedback and caps in-memory retention', () => {
    const first = mergeFeedback([], feedback);
    expect(mergeFeedback(first, { ...feedback, explanation: 'Updated' })).toHaveLength(1);
    expect(mergeFeedback(first, { ...feedback, explanation: 'Updated' })[0].explanation).toBe('Updated');
    const many = Array.from({ length: 80 }, (_, i) => ({ ...feedback, turn_id: String(i) }));
    expect(mergeFeedback(many, feedback)).toHaveLength(80);
    expect(mergeFeedback(many, feedback)[0].turn_id).toBe('1');
  });
});
