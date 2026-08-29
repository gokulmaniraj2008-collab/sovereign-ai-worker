from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.documents import router as documents_router
from app.api.rag import router as rag_router
from app.api.security import router as security_router
from app.database import get_conn

app = FastAPI(title=settings.app_name, version="0.1.2")
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
    """Report service and database health without exposing credentials."""
    if not settings.database_url.strip():
        return {
            "status": "degraded",
            "service": settings.app_name,
            "database": {
                "status": "unavailable",
                "error": "DATABASE_URL is not configured",
                "hint": "Set DATABASE_URL in the Render environment variables.",
            },
        }

    try:
        with get_conn() as conn:
            conn.execute("SELECT 1").fetchone()
            conn.execute("SELECT extname FROM pg_extension WHERE extname = 'vector'").fetchone()
        return {
            "status": "ok",
            "service": settings.app_name,
            "database": {
                "status": "connected",
                "provider": "PostgreSQL",
                "vector_extension": "available",
            },
        }
    except Exception as exc:
        message = str(exc).lower()
        if "password authentication failed" in message or "authentication failed" in message:
            error = "Database authentication failed"
            hint = "Verify the Supabase PostgreSQL username and password in DATABASE_URL."
        elif "timeout" in message or "timed out" in message:
            error = "Database connection timed out"
            hint = "Check Supabase connectivity or use the Supabase connection pooler."
        elif "could not translate host name" in message or "name or service not known" in message:
            error = "Database hostname could not be resolved"
            hint = "Verify the Supabase hostname in DATABASE_URL."
        elif "connection refused" in message:
            error = "Database connection refused"
            hint = "Verify DATABASE_URL is active in the running Render deployment and the database host/port are correct."
        elif "ssl" in message:
            error = "Database SSL connection failed"
            hint = "Use the SSL-enabled Supabase PostgreSQL connection string."
        else:
            error = "Database connection failed"
            hint = "Check DATABASE_URL, SSL settings, and Supabase connectivity."

        return {
            "status": "degraded",
            "service": settings.app_name,
            "database": {
                "status": "unavailable",
                "error": error,
                "hint": hint,
            },
        }
