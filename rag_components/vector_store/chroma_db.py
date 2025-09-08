# rag_components/vector_store/chroma_db.py
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from typing import List, Tuple
from .base import BaseVectorDB
import uuid

class ChromaDBVectorStore(BaseVectorDB):
    def __init__(self, collection_name: str, embedding_model: str = "all-MiniLM-L6-v2"):
        self.client = chromadb.Client(Settings(
            persist_directory="chroma_store"  # local persistence
        ))
        self.embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=embedding_model
        )
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_func
        )

    def add_documents(self, documents: List[str], ids: List[str] = None):
        if ids is None:
            ids = [str(uuid.uuid4()) for _ in documents]
        self.collection.add(documents=documents, ids=ids)

    def query(self, query: str, top_k: int = 5) -> List[Tuple[str, float]]:
        results = self.collection.query(
            query_texts=[query],
            n_results=top_k
        )
        docs = results["documents"][0]
        scores = results["distances"][0]
        return list(zip(docs, scores))

    def persist(self, path: str = None):
        self.client.persist()

    def load(self, path: str = None):
        # Chroma auto-handles persistence, so just reload
        self.client = chromadb.Client(Settings(
            persist_directory="chroma_store"
        ))
