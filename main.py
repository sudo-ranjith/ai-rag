from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import uvicorn
from api import router as api_router

# Load env
load_dotenv()

# FastAPI app
app = FastAPI(
    title="LangChain RAG API",
    description="RAG application supporting text files (Phase 1)",
    version="1.0.0"
)

# Include API
app.include_router(api_router, prefix="/rag", tags=["RAG"])

# Exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": str(exc)})

# Run app
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
