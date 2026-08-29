from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).resolve().parents[2]
STORAGE_DIR = ROOT.parent / "storage"


class Settings(BaseSettings):
    app_name: str = "SovereignAI Worker"
    # Render/Supabase supplies DATABASE_URL at runtime. This fallback is for local Docker only.
    database_url: str = "postgresql://sovereign:sovereign@localhost:5433/sovereign"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.2:3b"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    embedding_dimension: int = 384
    chunk_size: int = 900
    chunk_overlap: int = 120
    upload_dir: str = str(STORAGE_DIR / "documents")
    processed_dir: str = str(STORAGE_DIR / "processed")
    cors_origins: str = "http://localhost:3000"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()
Path(settings.upload_dir).mkdir(parents=True, exist_ok=True)
Path(settings.processed_dir).mkdir(parents=True, exist_ok=True)
