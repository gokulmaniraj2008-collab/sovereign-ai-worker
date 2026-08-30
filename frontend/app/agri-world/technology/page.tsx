import Link from 'next/link';

const stack = ['React','TypeScript','Vite','Three.js','React Three Fiber','Supabase'];

export default function TechnologyPage() {
  return <main className="shell"><header><div><h1>AGRI-WORLD — TECHNOLOGY</h1><p>The planned stack for the 3D agricultural experience.</p></div><Link href="/agri-world" className="badge">← AGRI-WORLD</Link></header><section className="card"><h2>Technology Stack</h2><div className="row" style={{flexWrap:'wrap',gap:10,marginTop:16}}>{stack.map(tech=><span className="source" key={tech}>{tech}</span>)}</div></section><section className="card"><h2>Architecture</h2><p>Frontend rendering uses React and Three.js/React Three Fiber. Supabase can provide persistence for player progress, project data and connected systems.</p></section></main>;
}
