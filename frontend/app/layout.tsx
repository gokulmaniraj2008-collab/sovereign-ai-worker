import './globals.css';
export const metadata = { title: 'SovereignAI Worker', description: 'Local-first enterprise AI workspace' };
export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) { return <html lang="en"><body>{children}</body></html>; }
