from functools import lru_cache
from app.config import settings


class EmbeddingProvider:
    def embed(self, texts: list[str]) -> list[list[float]]:
        raise NotImplementedError


class LocalEmbeddingProvider(EmbeddingProvider):
    @property
    @lru_cache(maxsize=1)
    def model(self):
        # Lazy import keeps FastAPI startup lightweight so Render can detect
        # the HTTP port before the ML stack is initialized. The model is still
        # loaded locally on the first embedding request and then cached.
        from sentence_transformers import SentenceTransformer
        return SentenceTransformer(settings.embedding_model)

    def embed(self, texts: list[str]) -> list[list[float]]:
        return self.model.encode(texts, normalize_embeddings=True).tolist()


embedding_provider = LocalEmbeddingProvider()
