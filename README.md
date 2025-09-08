# 🚀 RAG Application (Phase 1: Text Files)

This project is a **Retrieval-Augmented Generation (RAG) application** built with **FastAPI** and **ChromaDB**.  
In **Phase 1**, the app supports ingestion and querying of **text files**.  
Future phases will extend to **PDFs** and **image-based math books**.

---

## ✨ Features
- 📂 Upload `.txt` files and index them in **ChromaDB**.
- 🔍 Query the vector database with natural language questions.
- 🧩 Modular **OOP-ready design** (easy to switch to FAISS, Pinecone, Weaviate, etc.).
- ⚡ Powered by **FastAPI** with automatic Swagger UI.

---

## 📂 Project Structure
AI-RAG/
│── data/ # Input files storage
│── rag_components/ # RAG logic modules
│ │── chunker.py # File chunking utilities
│ │── repository.py # Data ingestion logic
│ │── service.py # RAG service layer
│ │── vector_store/ # Vector DB abstractions
│── .env # Environment variables
│── .gitignore # Git ignore rules
│── api.py # API routes
│── config.py # Config and settings
│── main.py # FastAPI entrypoint
│── rag_chain.py # RAG pipeline logic
│── requirements.txt # Dependencies
│── README.md # Documentation


---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-rag.git
cd ai-rag


2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate       # Windows


3. Install dependencies
pip install -r requirements.txt

4. Create .env file
# .env
VECTOR_STORE_TYPE=chroma
EMBEDDING_MODEL_NAME=all-MiniLM-L6-v2
CHUNK_SIZE=500
CHUNK_OVERLAP=50
DOCS_PATH=data/

5. Run the FastAPI app
uvicorn main:app --reload

🌐 API Endpoints
Swagger Docs

👉 http://127.0.0.1:8000/docs

1. Upload Text File

POST /rag/upload-text

curl -X POST "http://127.0.0.1:8000/rag/upload-text" \
     -F "file=@data/notes.txt"


Response:

{
  "message": "notes.txt uploaded and indexed successfully"
}

2. Query the RAG System

POST /rag/query

curl -X POST "http://127.0.0.1:8000/rag/query" \
     -H "Content-Type: application/json" \
     -d '{"question": "What is machine learning?"}'


Response:

{
  "answer": "Machine learning is ..."
}

✅ Roadmap

 Phase 2 → Add PDF ingestion.

 Phase 3 → Add Image/Math OCR support.

 Phase 4 → Integrate with LLMs (OpenAI, Llama, etc.) for better answer synthesis.

💡 Author

👨‍💻 Built by Ranjith Kumar – passionate about AI, RAG, and agentic systems.