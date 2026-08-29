import httpx
from app.config import settings
class LLMProvider:
    def generate(self,prompt:str)->str: raise NotImplementedError
class LocalLLMProvider(LLMProvider):
    def generate(self,prompt:str)->str:
        r=httpx.post(f"{settings.ollama_base_url.rstrip('/')}/api/generate",json={"model":settings.ollama_model,"prompt":prompt,"stream":False},timeout=180); r.raise_for_status(); return r.json()["response"].strip()
llm_provider=LocalLLMProvider()
