# rag_components/vector_store/base.py
from abc import ABC, abstractmethod
from typing import List, Tuple

class BaseVectorDB(ABC):
    @abstractmethod
    def add_documents(self, documents: List[str], ids: List[str] = None):
        """Add documents (with optional IDs) into the vector store"""
        pass

    @abstractmethod
    def query(self, query: str, top_k: int = 5) -> List[Tuple[str, float]]:
        """Query the vector store and return (document, score) pairs"""
        pass

    @abstractmethod
    def persist(self, path: str):
        """Save the vector database to disk"""
        pass

    @abstractmethod
    def load(self, path: str):
        """Load the vector database from disk"""
        pass
