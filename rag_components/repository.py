# rag_components/repository.py
from pathlib import Path

class TextRepository:
    def __init__(self, docs_path: str = "data/"):
        self.docs_path = Path(docs_path)

    def load_text_file(self, file_name: str) -> str:
        file_path = self.docs_path / file_name
        if not file_path.exists():
            raise FileNotFoundError(f"{file_name} not found in {self.docs_path}")
        return file_path.read_text(encoding="utf-8")
