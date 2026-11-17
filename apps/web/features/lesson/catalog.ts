/** Public display data. Curriculum and worker prompts remain server-owned. */
export const LESSONS = [
  {
    id: 'mock-interview',
    title: 'Mock interview',
    heading: 'A little more interview-ready.',
    description: 'Talk about your experience, practice your answers, and build confidence for your next interview.',
    badge: 'MOCK INTERVIEW',
  },
  {
    id: 'everyday-conversation',
    title: 'Everyday English',
    heading: 'A friendly chat. A little more confidence.',
    description: 'Talk about your day, hobbies, and small everyday moments with a patient AI practice partner.',
    badge: 'EVERYDAY ENGLISH',
  },
  {
    id: 'cafe-order',
    title: 'Café order',
    heading: 'Order at a café in English.',
    description: 'Ask for a drink, explain how you’d like it, and choose another option if it’s sold out.',
    badge: 'CAFÉ ORDER',
  },
] as const;

export type LessonId = typeof LESSONS[number]['id'];
export type LessonChoice = typeof LESSONS[number];
export const DEFAULT_LESSON_ID: LessonId = 'mock-interview';

export function findLesson(id: unknown): LessonChoice | undefined {
  return typeof id === 'string' ? LESSONS.find((lesson) => lesson.id === id) : undefined;
}
