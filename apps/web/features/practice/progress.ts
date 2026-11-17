import { ACTIVITIES } from './activities';

export const PROGRESS_KEY = 'eng-teacher:practice-progress';
const PROGRESS_VERSION = 1;

interface ActivityProgress {
  draft: boolean[] | null;
  latestScore: number | null;
  attempts: number;
}

export interface PracticeProgress {
  activities: Record<string, ActivityProgress>;
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value);
}

function validResults(value: unknown, min: number, max: number): value is boolean[] {
  return Array.isArray(value)
    && value.length >= min
    && value.length <= max
    && Array.from(value).every((result) => typeof result === 'boolean');
}

function parseActivity(value: unknown, exerciseCount: number): ActivityProgress | null {
  if (!isRecord(value) || Object.keys(value).length !== 3) return null;
  const { draft, latestScore, attempts } = value;
  if (draft !== null && !validResults(draft, 1, exerciseCount - 1)) return null;
  if (typeof attempts !== 'number' || !Number.isSafeInteger(attempts) || attempts < 0) return null;
  if (latestScore !== null && (
    typeof latestScore !== 'number'
    || !Number.isInteger(latestScore)
    || latestScore < 0
    || latestScore > exerciseCount
  )) return null;
  if ((latestScore === null) !== (attempts === 0)) return null;
  return { draft, latestScore, attempts };
}

export function readProgress(storage: Pick<Storage, 'getItem'>): PracticeProgress | null {
  const raw = storage.getItem(PROGRESS_KEY);
  if (raw === null) return null;

  let value: unknown;
  try {
    value = JSON.parse(raw);
  } catch {
    return null;
  }
  if (!isRecord(value) || Object.keys(value).length !== 2
    || value.version !== PROGRESS_VERSION || !isRecord(value.activities)) return null;

  const progress: PracticeProgress = { activities: {} };
  for (const [id, record] of Object.entries(value.activities)) {
    const activity = ACTIVITIES.find((item) => item.id === id);
    if (!activity) return null;
    const parsed = parseActivity(record, activity.exercises.length);
    if (!parsed) return null;
    progress.activities[id] = parsed;
  }
  return progress;
}

function writeProgress(
  storage: Pick<Storage, 'setItem'>, progress: PracticeProgress,
): PracticeProgress {
  storage.setItem(PROGRESS_KEY, JSON.stringify({
    version: PROGRESS_VERSION,
    activities: progress.activities,
  }));
  return progress;
}

export function enableProgress(storage: Pick<Storage, 'getItem' | 'setItem'>): PracticeProgress {
  return readProgress(storage) ?? writeProgress(storage, { activities: {} });
}

export function clearProgress(storage: Pick<Storage, 'removeItem'>): void {
  storage.removeItem(PROGRESS_KEY);
}

export function saveProgress(
  storage: Pick<Storage, 'getItem' | 'setItem'>,
  activityId: string,
  results: boolean[],
  completed: boolean,
): PracticeProgress | null {
  const progress = readProgress(storage);
  if (!progress) return null;

  const activity = ACTIVITIES.find((item) => item.id === activityId);
  if (!activity || typeof completed !== 'boolean') return progress;
  const count = activity.exercises.length;
  if (!validResults(results, completed ? count : 1, completed ? count : count - 1)) return progress;

  const previous = progress.activities[activityId] ?? { draft: null, latestScore: null, attempts: 0 };
  progress.activities[activityId] = completed
    ? {
      draft: null,
      latestScore: results.filter(Boolean).length,
      attempts: Math.min(previous.attempts + 1, Number.MAX_SAFE_INTEGER),
    }
    : { ...previous, draft: [...results] };
  return writeProgress(storage, progress);
}
