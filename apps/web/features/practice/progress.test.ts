import { describe, expect, it, vi } from 'vitest';
import {
  PROGRESS_KEY, clearProgress, enableProgress, readProgress, saveProgress,
} from './progress';

function memoryStorage() {
  const values = new Map<string, string>();
  return {
    getItem: vi.fn((key: string) => values.get(key) ?? null),
    setItem: vi.fn((key: string, value: string) => { values.set(key, value); }),
    removeItem: vi.fn((key: string) => { values.delete(key); }),
  };
}

describe('opt-in practice progress', () => {
  it('saves nothing until enabled and writes just one versioned key', () => {
    const storage = memoryStorage();
    expect(readProgress(storage)).toBeNull();
    expect(saveProgress(storage, 'work-update', [true], false)).toBeNull();
    expect(storage.setItem).not.toHaveBeenCalled();

    expect(enableProgress(storage)).toEqual({ activities: {} });
    expect(storage.setItem).toHaveBeenCalledExactlyOnceWith(
      PROGRESS_KEY, JSON.stringify({ version: 1, activities: {} }),
    );
    expect(readProgress(storage)).toEqual({ activities: {} });
  });

  it('stores partial correctness, then replaces it with the latest score and attempt count', () => {
    const storage = memoryStorage();
    enableProgress(storage);
    const draft = [true, false];
    expect(saveProgress(storage, 'work-update', draft, false)).toEqual({
      activities: { 'work-update': { draft: [true, false], latestScore: null, attempts: 0 } },
    });
    draft[0] = false;
    expect(readProgress(storage)?.activities['work-update'].draft).toEqual([true, false]);
    expect(saveProgress(storage, 'work-update', [true, false, true], true)).toEqual({
      activities: { 'work-update': { draft: null, latestScore: 2, attempts: 1 } },
    });

    saveProgress(storage, 'train-platform', [false], false);
    saveProgress(storage, 'work-update', [false], false);
    expect(readProgress(storage)?.activities['work-update']).toEqual({
      draft: [false], latestScore: 2, attempts: 1,
    });
    expect(saveProgress(storage, 'work-update', [false, false, false], true)).toEqual({
      activities: {
        'work-update': { draft: null, latestScore: 0, attempts: 2 },
        'train-platform': { draft: [false], latestScore: null, attempts: 0 },
      },
    });
    expect(JSON.parse(storage.getItem(PROGRESS_KEY)!)).toEqual({
      version: 1,
      activities: {
        'work-update': { draft: null, latestScore: 0, attempts: 2 },
        'train-platform': { draft: [false], latestScore: null, attempts: 0 },
      },
    });

    storage.setItem.mockClear();
    expect(enableProgress(storage)).toEqual(readProgress(storage));
    expect(storage.setItem).not.toHaveBeenCalled();
  });

  it('removes saved progress without affecting other browser storage or recreating the key', () => {
    const storage = memoryStorage();
    storage.setItem('unrelated', 'keep');
    enableProgress(storage);
    saveProgress(storage, 'work-update', [true], false);

    clearProgress(storage);
    expect(storage.removeItem).toHaveBeenCalledExactlyOnceWith(PROGRESS_KEY);
    expect(readProgress(storage)).toBeNull();
    expect(saveProgress(storage, 'work-update', [true, true, true], true)).toBeNull();
    expect(storage.getItem(PROGRESS_KEY)).toBeNull();
    expect(storage.getItem('unrelated')).toBe('keep');
    expect(enableProgress(storage)).toEqual({ activities: {} });
  });

  it.each([
    '{invalid json',
    'null',
    '{"version":2,"activities":{}}',
    '{"version":1,"activities":[]}',
    '{"version":1,"activities":{},"email":"unexpected"}',
    '{"version":1,"activities":{"__proto__":{"draft":[true],"latestScore":null,"attempts":0}}}',
    '{"version":1,"activities":{"work-update":{"draft":[],"latestScore":null,"attempts":0}}}',
    '{"version":1,"activities":{"work-update":{"draft":[true,true,true],"latestScore":null,"attempts":0}}}',
    '{"version":1,"activities":{"work-update":{"draft":[1],"latestScore":null,"attempts":0}}}',
    '{"version":1,"activities":{"work-update":{"draft":null,"latestScore":4,"attempts":1}}}',
    '{"version":1,"activities":{"work-update":{"draft":null,"latestScore":2,"attempts":0}}}',
    '{"version":1,"activities":{"work-update":{"draft":null,"latestScore":null,"attempts":1}}}',
    '{"version":1,"activities":{"work-update":{"draft":[true],"latestScore":null,"attempts":-1}}}',
    '{"version":1,"activities":{"work-update":{"draft":null,"latestScore":2,"attempts":1.5}}}',
    '{"version":1,"activities":{"work-update":{"draft":[true],"latestScore":null,"attempts":0,"answer":"unexpected"}}}',
  ])('treats invalid or unsupported records as disabled without modifying storage', (raw) => {
    const storage = memoryStorage();
    storage.setItem(PROGRESS_KEY, raw);
    expect(readProgress(storage)).toBeNull();
    expect(saveProgress(storage, 'work-update', [true], false)).toBeNull();
    expect(storage.getItem(PROGRESS_KEY)).toBe(raw);
  });

  it('leaves enabled storage unchanged for invalid IDs, lengths and result types', () => {
    const storage = memoryStorage();
    enableProgress(storage);
    const initial = saveProgress(storage, 'work-update', [true], false);
    storage.setItem.mockClear();

    expect(saveProgress(storage, 'unknown', [true], false)).toEqual(initial);
    expect(saveProgress(storage, 'work-update', [], false)).toEqual(initial);
    expect(saveProgress(storage, 'work-update', [true, true], true)).toEqual(initial);
    expect(saveProgress(storage, 'work-update', [true, true, true], false)).toEqual(initial);
    expect(saveProgress(storage, 'work-update', [false, false, false, false], true)).toEqual(initial);
    expect(saveProgress(storage, 'work-update', [1 as unknown as boolean], false)).toEqual(initial);
    expect(saveProgress(storage, 'work-update', new Array<boolean>(1), false)).toEqual(initial);
    expect(storage.setItem).not.toHaveBeenCalled();
  });

  it('lets storage errors reach callers so the UI can handle unavailable storage', () => {
    const storage = memoryStorage();
    const failure = new Error('storage unavailable');
    storage.setItem.mockImplementation(() => { throw failure; });
    storage.removeItem.mockImplementation(() => { throw failure; });
    expect(() => enableProgress(storage)).toThrow(failure);
    expect(() => clearProgress(storage)).toThrow(failure);

    storage.getItem.mockImplementation(() => { throw failure; });
    expect(() => readProgress(storage)).toThrow(failure);
    expect(() => saveProgress(storage, 'work-update', [true], false)).toThrow(failure);
  });
});
