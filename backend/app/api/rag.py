from uuid import uuid4
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.config import settings
from app.database import get_conn
from app.services.retrieval import search_chunks
from app.services.citations import build_sources
from app.services.llm import llm_provider
router=APIRouter(prefix="/rag",tags=["rag"])
class QueryRequest(BaseModel): query:str
@router.post("/query")
def query_rag(payload:QueryRequest):
    if not payload.query.strip(): raise HTTPException(400,"Query is required")
    rows=search_chunks(payload.query,limit=5)
    if not rows: return {"answer":"No indexed evidence was found.","model":settings.ollama_model,"sources":[]}
    context="\n\n".join(f"[Source {i+1}: {r['filename']} p.{r['page_number']}]\n{r['content']}" for i,r in enumerate(rows))
    prompt=f"You are a local enterprise document analyst. Answer only from the evidence below. If evidence is insufficient, say so. Cite sources inline as [Source N].\n\nQUESTION:\n{payload.query}\n\nEVIDENCE:\n{context}"
    answer=llm_provider.generate(prompt); query_id=uuid4()
    with get_conn() as conn:
        conn.execute("INSERT INTO rag_queries (id,query,answer) VALUES (%s,%s,%s)",(query_id,payload.query,answer))
        for r in rows: conn.execute("INSERT INTO evidence (id,query_id,chunk_id,relevance) VALUES (%s,%s,%s,%s)",(uuid4(),query_id,r["id"],r["relevance"]))
        conn.execute("INSERT INTO audit_logs (id,event_type,component,details) VALUES (%s,%s,%s,%s)",(uuid4(),"rag_query","local_rag",{"query_id":str(query_id),"model":settings.ollama_model})); conn.commit()
    return {"answer":answer,"model":settings.ollama_model,"sources":build_sources(rows)}
