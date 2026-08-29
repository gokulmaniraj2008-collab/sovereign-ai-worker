from pathlib import Path
from uuid import uuid4
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.config import settings
from app.database import get_conn
from app.services.extraction import extract_pdf
from app.services.ocr import ocr_pdf
from app.services.embeddings import embedding_provider
router = APIRouter(prefix="/documents", tags=["documents"])
@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if file.content_type != "application/pdf": raise HTTPException(400,"Phase 1 accepts PDF files only")
    document_id=uuid4(); path=Path(settings.upload_dir)/f"{document_id}.pdf"; path.write_bytes(await file.read())
    with get_conn() as conn:
        conn.execute("INSERT INTO documents (id,filename,mime_type,file_path) VALUES (%s,%s,%s,%s)",(document_id,file.filename,file.content_type,str(path))); conn.commit()
    return {"id":str(document_id),"filename":file.filename,"status":"uploaded"}
@router.post("/{document_id}/ingest")
def ingest_document(document_id:str):
    with get_conn() as conn: doc=conn.execute("SELECT * FROM documents WHERE id=%s",(document_id,)).fetchone()
    if not doc: raise HTTPException(404,"Document not found")
    pages=extract_pdf(doc["file_path"])
    if not any(p["text"] for p in pages): pages=ocr_pdf(doc["file_path"])
    chunks=[]
    for page in pages:
        words=page["text"].split()
        for start in range(0,len(words),settings.chunk_size):
            content=" ".join(words[start:start+settings.chunk_size]).strip()
            if content: chunks.append((page["page_number"],content))
    vectors=embedding_provider.embed([c for _,c in chunks]) if chunks else []
    with get_conn() as conn:
        conn.execute("DELETE FROM document_chunks WHERE document_id=%s",(document_id,))
        for i,((page,content),vector) in enumerate(zip(chunks,vectors)):
            conn.execute("INSERT INTO document_chunks (id,document_id,content,page_number,chunk_index,embedding) VALUES (%s,%s,%s,%s,%s,%s)",(uuid4(),document_id,content,page,i,vector))
        conn.execute("UPDATE documents SET status='ingested' WHERE id=%s",(document_id,)); conn.commit()
    return {"document_id":document_id,"status":"ingested","pages":len(pages),"chunks":len(chunks)}
@router.get("")
def list_documents():
    with get_conn() as conn: return conn.execute("SELECT id,filename,mime_type,status,created_at FROM documents ORDER BY created_at DESC").fetchall()
