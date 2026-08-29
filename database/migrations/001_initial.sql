CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE IF NOT EXISTS documents (id UUID PRIMARY KEY,filename TEXT NOT NULL,mime_type TEXT NOT NULL,file_path TEXT NOT NULL,status TEXT NOT NULL DEFAULT 'uploaded',created_at TIMESTAMPTZ DEFAULT now());
CREATE TABLE IF NOT EXISTS document_chunks (id UUID PRIMARY KEY,document_id UUID NOT NULL REFERENCES documents(id) ON DELETE CASCADE,content TEXT NOT NULL,page_number INTEGER,chunk_index INTEGER NOT NULL,embedding vector(384),created_at TIMESTAMPTZ DEFAULT now());
CREATE TABLE IF NOT EXISTS models (id UUID PRIMARY KEY,name TEXT NOT NULL,provider TEXT NOT NULL,model_type TEXT NOT NULL,local_only BOOLEAN NOT NULL DEFAULT TRUE,active BOOLEAN NOT NULL DEFAULT TRUE);
CREATE TABLE IF NOT EXISTS rag_queries (id UUID PRIMARY KEY,query TEXT NOT NULL,model_id UUID REFERENCES models(id),answer TEXT,created_at TIMESTAMPTZ DEFAULT now());
CREATE TABLE IF NOT EXISTS evidence (id UUID PRIMARY KEY,query_id UUID NOT NULL REFERENCES rag_queries(id) ON DELETE CASCADE,chunk_id UUID NOT NULL REFERENCES document_chunks(id),relevance REAL,created_at TIMESTAMPTZ DEFAULT now());
CREATE TABLE IF NOT EXISTS audit_logs (id UUID PRIMARY KEY,event_type TEXT NOT NULL,component TEXT NOT NULL,details JSONB,created_at TIMESTAMPTZ DEFAULT now());
CREATE INDEX IF NOT EXISTS document_chunks_embedding_idx ON document_chunks USING hnsw (embedding vector_cosine_ops);
