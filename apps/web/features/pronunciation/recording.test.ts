import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { MAX_RECORDING_SECONDS, recordLearnerAudio } from './recording';

class TestRecorder {
  static instance: TestRecorder;
  state = 'inactive';
  mimeType = 'audio/webm';
  ondataavailable: ((event: { data: Blob }) => void) | null = null;
  onstop: (() => void) | null = null;
  onerror: (() => void) | null = null;

  constructor() {
    TestRecorder.instance = this;
  }

  start() {
    this.state = 'recording';
  }

  stop() {
    this.state = 'inactive';
    queueMicrotask(() => {
      this.ondataavailable?.({ data: new Blob(['audio']) });
      this.onstop?.();
    });
  }
}

describe('local self-listening capture', () => {
  const stopTrack = vi.fn();
  const stream = { getTracks: () => [{ stop: stopTrack }] } as unknown as MediaStream;
  const getUserMedia = vi.fn<() => Promise<MediaStream>>();

  beforeEach(() => {
    stopTrack.mockClear();
    getUserMedia.mockReset().mockResolvedValue(stream);
    vi.stubGlobal('navigator', { mediaDevices: { getUserMedia } });
    vi.stubGlobal('MediaRecorder', TestRecorder);
  });

  afterEach(() => {
    vi.unstubAllGlobals();
    vi.useRealTimers();
  });

  it('requests audio only and releases the microphone before returning the clip', async () => {
    const capture = recordLearnerAudio(new AbortController().signal, (stop) => {
      expect(stopTrack).not.toHaveBeenCalled();
      stop();
      expect(stopTrack).toHaveBeenCalledOnce();
    });
    expect(getUserMedia).toHaveBeenCalledWith({ audio: true });
    const clip = await capture;
    expect(clip.type).toBe('audio/webm');
    expect(await clip.text()).toBe('audio');
    expect(stopTrack).toHaveBeenCalledOnce();
  });

  it('stops automatically at the time limit', async () => {
    vi.useFakeTimers();
    const started = vi.fn();
    const capture = recordLearnerAudio(new AbortController().signal, started);
    await Promise.resolve();
    expect(started).toHaveBeenCalledOnce();
    await vi.advanceTimersByTimeAsync(MAX_RECORDING_SECONDS * 1000 - 1);
    expect(stopTrack).not.toHaveBeenCalled();
    await vi.advanceTimersByTimeAsync(1);
    expect(await capture).toBeInstanceOf(Blob);
    expect(stopTrack).toHaveBeenCalledOnce();
  });

  it('stops a late permission grant when the learner already left', async () => {
    const permission = Promise.withResolvers<MediaStream>();
    getUserMedia.mockReturnValueOnce(permission.promise);
    const canceled = new AbortController();
    const started = vi.fn();
    const capture = recordLearnerAudio(canceled.signal, started);
    const rejection = expect(capture).rejects.toMatchObject({ name: 'AbortError' });
    canceled.abort();
    permission.resolve(stream);
    await rejection;
    expect(started).not.toHaveBeenCalled();
    expect(stopTrack).toHaveBeenCalledOnce();
  });

  it('discards an active clip when the learner cancels', async () => {
    const canceled = new AbortController();
    const capture = recordLearnerAudio(canceled.signal, () => canceled.abort());
    await expect(capture).rejects.toMatchObject({ name: 'AbortError' });
    expect(TestRecorder.instance.state).toBe('inactive');
    expect(TestRecorder.instance.ondataavailable).toBeNull();
    expect(stopTrack).toHaveBeenCalledOnce();
  });

  it('gives readable fallbacks when recording is unavailable', async () => {
    getUserMedia.mockRejectedValueOnce(new DOMException('internal error', 'NotAllowedError'));
    await expect(recordLearnerAudio(new AbortController().signal, vi.fn())).rejects.toThrow('Check permissions');
    vi.stubGlobal('MediaRecorder', undefined);
    await expect(recordLearnerAudio(new AbortController().signal, vi.fn())).rejects.toThrow('This browser cannot record');
    expect(getUserMedia).toHaveBeenCalledOnce();
  });

  it('releases tracks if the recorder reports a failure', async () => {
    const capture = recordLearnerAudio(new AbortController().signal, () => TestRecorder.instance.onerror?.());
    await expect(capture).rejects.toThrow('The browser stopped recording');
    expect(TestRecorder.instance.state).toBe('inactive');
    expect(stopTrack).toHaveBeenCalledOnce();
  });
});
