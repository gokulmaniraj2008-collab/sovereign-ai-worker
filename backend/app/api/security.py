from fastapi import APIRouter
from app.config import settings
router=APIRouter(prefix="/security",tags=["security"])
@router.get("/status")
def security_status():
    local=settings.ollama_base_url.startswith(("http://localhost","http://127.0.0.1","http://ollama:"))
    return {"mode":"local-first","internet_required_for_core_pipeline":False,"cloud_llm":False,"local_llm_endpoint":settings.ollama_base_url,"local_llm_configured":local,"local_storage":True,"local_embeddings":True,"local_ocr":True,"database":"PostgreSQL + pgvector"}
