interface Exercise {
  focus: 'Grammar' | 'Vocabulary' | 'Conversation';
  prompt: string;
  options: readonly [string, string, string];
  correct: 0 | 1 | 2;
  explanation: string;
}

export interface Activity {
  id: string;
  title: string;
  description: string;
  exercises: readonly [Exercise, ...Exercise[]];
  speakingPrompt: string;
  example: string;
}

export const ACTIVITIES: readonly Activity[] = [
  {
    id: 'work-update',
    title: 'Give a work update',
    description: 'Say what you finished, explain a delay and offer a next step.',
    exercises: [
      {
        focus: 'Grammar',
        prompt: 'You finished checking the figures yesterday. Which sentence gives that update?',
        options: ['I check the figures yesterday.', 'I checked the figures yesterday.', 'I will check the figures yesterday.'],
        correct: 1,
        explanation: 'Use the simple past with a finished time such as “yesterday”.',
      },
      {
        focus: 'Vocabulary',
        prompt: 'The team cannot see your draft until you get the files you need. What would you say?',
        options: ['The draft is ready to send.', 'The draft is on schedule.', 'The draft is on hold.'],
        correct: 2,
        explanation: '“On hold” means temporarily paused. You can add what needs to happen before you continue.',
      },
      {
        focus: 'Conversation',
        prompt: 'You can send a draft today and finish the full report tomorrow. Which reply makes both commitments clear?',
        options: ['I can send a draft today and the full report tomorrow.', 'I’ll send both the draft and the full report today.', 'I’ll send something when it’s ready.'],
        correct: 0,
        explanation: 'Name both deliverables and give a time for each so the listener knows what to expect.',
      },
    ],
    speakingPrompt: 'Think of a task you worked on. Say one thing you finished, one thing still pending and when you can give another update.',
    example: 'I checked the figures this morning. I’m waiting for one file, and I can give you another update at three.',
  },
  {
    id: 'train-platform',
    title: 'Find the right train',
    description: 'Ask for directions, understand a station announcement and check a detail.',
    exercises: [
      {
        focus: 'Grammar',
        prompt: 'You want to ask for the next train’s departure time. Which question fits?',
        options: ['What time the next train leaves?', 'What time does the next train leaves?', 'What time does the next train leave?'],
        correct: 2,
        explanation: 'After “does”, use the base form “leave”.',
      },
      {
        focus: 'Vocabulary',
        prompt: 'The announcement says your train “has been delayed”. What does that mean?',
        options: ['It will leave later than scheduled.', 'It will leave from a different platform.', 'It has already left.'],
        correct: 0,
        explanation: 'A delay changes the expected time. A platform change is a separate announcement.',
      },
      {
        focus: 'Conversation',
        prompt: 'You heard that the platform changed, but missed the new number. What should you ask?',
        options: ['Did the train leave early?', 'Could you tell me the new platform number, please?', 'Could you change the platform, please?'],
        correct: 1,
        explanation: 'Ask for the specific information you missed. “Could you tell me…” makes the request polite and clear.',
      },
    ],
    speakingPrompt: 'Imagine your train is delayed. Ask for the new departure time and check whether it still leaves from the same platform.',
    example: 'What time does the train leave now? Does it still leave from platform two?',
  },
];
