import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Vector store type (e.g., "chroma", "faiss")
VECTOR_STORE_TYPE = os.getenv("VECTOR_STORE_TYPE", "chroma")

# Embedding model for Chroma
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "all-MiniLM-L6-v2")

# Chunking parameters
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 50))

# Document storage
DOCS_PATH = os.getenv("DOCS_PATH", "data/")
