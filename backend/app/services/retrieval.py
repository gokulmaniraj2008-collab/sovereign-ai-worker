from app.database import get_conn
from app.services.embeddings import embedding_provider
def search_chunks(query:str,limit:int=5):
    vector=embedding_provider.embed([query])[0]
    with get_conn() as conn:
        return conn.execute("SELECT dc.id,dc.document_id,dc.content,dc.page_number,d.filename,1-(dc.embedding <=> %s::vector) AS relevance FROM document_chunks dc JOIN documents d ON d.id=dc.document_id WHERE dc.embedding IS NOT NULL ORDER BY dc.embedding <=> %s::vector LIMIT %s",(vector,vector,limit)).fetchall()
