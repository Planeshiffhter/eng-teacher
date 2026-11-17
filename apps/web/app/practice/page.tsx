import type { Metadata } from 'next';
import { PracticeApp } from '@/features/practice/practice-app';

export const metadata: Metadata = {
  title: 'Quick exercises · Eng Teacher',
  description: 'Practice useful English through short grammar and vocabulary exercises.',
};

export default function PracticePage() {
  return <PracticeApp />;
}
