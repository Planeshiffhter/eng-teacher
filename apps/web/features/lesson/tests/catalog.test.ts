import { describe, expect, it } from 'vitest';
import contract from '../../../../../tests/contracts/lesson-catalog.json';
import { DEFAULT_LESSON_ID, LESSONS, findLesson } from '../catalog';

describe('public practice lesson catalog', () => {
  it('shares the worker contract and default', () => {
    expect(LESSONS.map((lesson) => lesson.id)).toEqual(contract.lesson_ids);
    expect(DEFAULT_LESSON_ID).toBe(contract.default_lesson_id);
    expect(findLesson('everyday-conversation')?.title).toBe('Everyday English');
    expect(findLesson('cafe-order')?.title).toBe('Café order');
  });
  it('does not accept user-defined prompts or prototype property names', () => {
    for (const value of [null, undefined, true, 1, {}, [], '', 'constructor', '__proto__', 'unknown']) {
      expect(findLesson(value)).toBeUndefined();
    }
  });
});
