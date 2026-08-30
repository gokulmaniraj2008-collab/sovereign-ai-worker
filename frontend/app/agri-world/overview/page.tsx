import Link from 'next/link';

export default function OverviewPage() {
  return <main className="shell"><header><div><h1>AGRI-WORLD — OVERVIEW</h1><p>Why the project exists and what it is designed to demonstrate.</p></div><Link href="/agri-world" className="badge">← AGRI-WORLD</Link></header><section className="card"><h2>Problem</h2><p>Agricultural concepts can be difficult to visualize through traditional learning alone. AGRI-WORLD turns those concepts into an interactive digital environment.</p></section><section className="card"><h2>Solution</h2><p>A 3D farming world with crop management, missions, agricultural robotics and AI-assisted guidance, designed with mobile interaction in mind.</p></section><section className="card"><h2>Goal</h2><p>Make agricultural technology more engaging while demonstrating how software, simulation, robotics and intelligent systems can work together.</p></section></main>;
}
