'use client';

import Link from 'next/link';

const sections = [
  ['Overview', '/agri-world/overview'],
  ['Features', '/agri-world/features'],
  ['Technology', '/agri-world/technology'],
  ['Roadmap', '/agri-world/roadmap'],
];

export default function AgriWorldPage() {
  return (
    <main className="shell">
      <header>
        <div>
          <p className="badge">AGRICULTURAL TECHNOLOGY</p>
          <h1>AGRI-WORLD</h1>
          <p>Interactive 3D agricultural simulation combining farming, robotics, AI and intelligent systems.</p>
        </div>
        <Link href="/" className="badge">← SovereignAI</Link>
      </header>
      <section className="card">
        <h2>AGRI-WORLD</h2>
        <p>Explore the project through separate pages instead of one long project description.</p>
        <div className="row" style={{flexWrap:'wrap', gap:12, marginTop:20}}>
          {sections.map(([name, href]) => <Link key={href} href={href} className="primary">{name}</Link>)}
        </div>
      </section>
      <section className="card">
        <h2>Project Vision</h2>
        <p>Build a mobile-friendly virtual agricultural world where users can learn farming concepts, manage crops, interact with agricultural robots and experiment with intelligent technology.</p>
      </section>
    </main>
  );
}
