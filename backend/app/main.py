from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.documents import router as documents_router
from app.api.rag import router as rag_router
from app.api.security import router as security_router
from app.database import get_conn

app = FastAPI(title=settings.app_name, version="0.1.1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[x.strip() for x in settings.cors_origins.split(",") if x.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(documents_router)
app.include_router(rag_router)
app.include_router(security_router)


@app.get("/health")
def health():
    # Verify the running deployment can reach its configured database.
    # Never expose DATABASE_URL or credentials in the response.
    try:
        with get_conn() as conn:
            conn.execute("SELECT 1").fetchone()
        return {"status": "ok", "service": settings.app_name, "database": "connected"}
    except Exception:
        return {"status": "degraded", "service": settings.app_name, "database": "unavailable"}
