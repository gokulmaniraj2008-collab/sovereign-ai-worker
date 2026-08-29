from sentence_transformers import SentenceTransformer
from functools import lru_cache
from app.config import settings
class EmbeddingProvider:
    def embed(self,texts:list[str])->list[list[float]]: raise NotImplementedError
class LocalEmbeddingProvider(EmbeddingProvider):
    @property
    @lru_cache(maxsize=1)
    def model(self): return SentenceTransformer(settings.embedding_model)
    def embed(self,texts:list[str])->list[list[float]]: return self.model.encode(texts,normalize_embeddings=True).tolist()
embedding_provider=LocalEmbeddingProvider()
