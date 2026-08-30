import Link from 'next/link';

const roadmap = [['01','Core 3D world','Terrain, farm plots, player movement and responsive controls.'],['02','Farming systems','Crop lifecycle, planting, growth, harvesting and missions.'],['03','AgriBot','Connect robot concepts and real-world agricultural workflows.'],['04','AI layer','Add intelligent guidance and contextual agricultural assistance.'],['05','Optimization','Improve mobile performance, loading and 3D asset efficiency.']];

export default function RoadmapPage() {
  return <main className="shell"><header><div><h1>AGRI-WORLD — ROADMAP</h1><p>Development stages from the foundation to an intelligent agricultural simulation.</p></div><Link href="/agri-world" className="badge">← AGRI-WORLD</Link></header><section className="card"><div>{roadmap.map(([num,title,desc])=><article className="source" key={num} style={{marginBottom:12}}><b>{num} · {title}</b><p>{desc}</p></article>)}</div></section></main>;
}
