import Link from 'next/link';

const features = ['3D farming environment','Crop management','Agricultural robot integration','AI assistant concept','Interactive missions','Mobile-first controls'];

export default function FeaturesPage() {
  return <main className="shell"><header><div><h1>AGRI-WORLD — FEATURES</h1><p>The main interactive systems planned for the experience.</p></div><Link href="/agri-world" className="badge">← AGRI-WORLD</Link></header><section className="card"><div className="row" style={{flexWrap:'wrap',gap:12}}>{features.map((feature,i)=><article className="source" key={feature}><b>{String(i+1).padStart(2,'0')}</b><p>{feature}</p></article>)}</div></section></main>;
}
