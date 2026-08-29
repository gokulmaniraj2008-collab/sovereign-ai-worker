from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.documents import router as documents_router
from app.api.rag import router as rag_router
from app.api.security import router as security_router
app = FastAPI(title=settings.app_name, version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=[x.strip() for x in settings.cors_origins.split(",") if x.strip()], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(documents_router)
app.include_router(rag_router)
app.include_router(security_router)
@app.get("/health")
def health(): return {"status":"ok","service":settings.app_name}
