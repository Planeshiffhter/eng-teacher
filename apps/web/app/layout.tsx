import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Eng Teacher · English speaking practice',
  description: 'Practice English with a ten-minute AI voice lesson or short grammar and vocabulary exercises.',
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}
