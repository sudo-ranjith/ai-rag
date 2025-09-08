# rag_components/service.py
from rag_components.chunker import TextChunker
from rag_components.repository import TextRepository
from rag_components.vector_store.chroma_db import ChromaDBVectorStore

class RAGService:
    def __init__(self, docs_path="data/", vector_db=None, chunk_size=500, overlap=50):
        self.repo = TextRepository(docs_path)
        self.chunker = TextChunker(chunk_size, overlap)
        self.vector_db = vector_db or ChromaDBVectorStore("rag_collection")

    def ingest_text_file(self, file_name: str):
        text = self.repo.load_text_file(file_name)
        chunks = self.chunker.chunk_text(text)
        self.vector_db.add_documents(chunks)

    def query(self, question: str, top_k: int = 5):
        return self.vector_db.query(question, top_k=top_k)
