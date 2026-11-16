export type FeedbackAction = 'correct' | 'clarify' | 'continue' | 'retry' | 'assist';
export interface TutorFeedback {
  version: 1;
  turn_id: string;
  original: string;
  corrected: string | null;
  explanation: string | null;
  action: FeedbackAction;
  spoken_response: string;
}
export interface LessonEvent {
  version: 1;
  state: 'started' | 'ended';
  deadline_ms: number;
  reason?: string;
}
export type TutorEvent =
  | { topic: 'tutor.feedback'; data: TutorFeedback }
  | { topic: 'tutor.lesson'; data: LessonEvent }
  | { topic: 'tutor.error'; data: { version: 1; message: string } };

const text = (value: unknown, max = 4_000): value is string =>
  typeof value === 'string' && value.length <= max;
const optionalText = (value: unknown): value is string | null => value === null || text(value);

/** All room data is untrusted. The caller also checks that the sender is the tutor. */
export function parseTutorEvent(payload: Uint8Array, topic?: string): TutorEvent | null {
  if (payload.byteLength > 20_000 || !topic?.startsWith('tutor.')) return null;
  try {
    const data: unknown = JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(payload));
    if (!data || typeof data !== 'object' || !('version' in data) || data.version !== 1) return null;
    const value = data as Record<string, unknown>;
    if (topic === 'tutor.feedback' && text(value.turn_id, 200) && value.turn_id.length > 0 &&
      text(value.original) && optionalText(value.corrected) && optionalText(value.explanation) &&
      text(value.spoken_response) && typeof value.action === 'string' && ['correct', 'clarify', 'continue', 'retry', 'assist'].includes(value.action) &&
      (value.action !== 'correct' || (typeof value.corrected === 'string' && value.corrected.trim().length > 0))) {
      return { topic, data: value as unknown as TutorFeedback };
    }
    if (topic === 'tutor.lesson' && typeof value.state === 'string' && ['started', 'ended'].includes(value.state) &&
      typeof value.deadline_ms === 'number' && Number.isSafeInteger(value.deadline_ms) &&
      value.deadline_ms > 0 && (value.reason === undefined || text(value.reason, 500))) {
      return { topic, data: value as unknown as LessonEvent };
    }
    if (topic === 'tutor.error' && text(value.message, 500) && value.message.length > 0) {
      return { topic, data: { version: 1, message: value.message } };
    }
  } catch { /* Invalid packets must never break the live audio session. */ }
  return null;
}

export const LESSON_SECONDS = 600;

/** A server event can shorten a lesson, but cannot extend the browser's cap. */
export function lessonDeadline(current: number, incoming: number): number {
  return Math.min(current, incoming);
}

export function secondsRemaining(deadline: number, now: number): number {
  return Math.max(0, Math.min(LESSON_SECONDS, Math.ceil((deadline - now) / 1_000)));
}

export function mergeFeedback(previous: TutorFeedback[], incoming: TutorFeedback): TutorFeedback[] {
  const index = previous.findIndex((item) => item.turn_id === incoming.turn_id);
  if (index < 0) return [...previous, incoming].slice(-80);
  return previous.map((item, i) => i === index ? incoming : item);
}
