from sentence_transformers import SentenceTransformer
import faiss
import os

class RAGChain:
    def __init__(self, model_name: str):
        self.model = SentenceTransformer(model_name)
        self.index = faiss.IndexFlatL2(384)  # embedding dim
        self.documents = []

    def add_document(self, text: str):
        embedding = self.model.encode([text])
        self.index.add(embedding)
        self.documents.append(text)

    def query(self, question: str, top_k: int = 3):
        embedding = self.model.encode([question])
        D, I = self.index.search(embedding, top_k)
        return [self.documents[i] for i in I[0]]
