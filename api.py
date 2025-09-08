from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
from rag_components.service import RAGService
import config
import shutil
from pathlib import Path

router = APIRouter()

# Initialize RAG Service (singleton style)
rag_service = RAGService(
    docs_path=config.DOCS_PATH,
    chunk_size=config.CHUNK_SIZE,
    overlap=config.CHUNK_OVERLAP
)

# Request/Response Schemas
class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str

@router.post("/upload-text")
async def upload_text(file: UploadFile = File(...)):
    try:
        # Save file into docs folder
        file_path = Path(config.DOCS_PATH) / file.filename
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Ingest into vector store
        rag_service.ingest_text_file(file.filename)
        return {"message": f"{file.filename} uploaded and indexed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    try:
        results = rag_service.query(request.question, top_k=3)
        # For MVP: just return top document, later we’ll call LLM
        if results:
            best_doc, score = results[0]
            return QueryResponse(answer=best_doc)
        else:
            return QueryResponse(answer="No relevant context found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
