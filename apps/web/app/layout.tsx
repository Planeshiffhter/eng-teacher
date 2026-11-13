import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Eng Teacher · Interview practice',
  description: 'A ten-minute Hindi–English speaking lesson with your AI interview tutor.',
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}
