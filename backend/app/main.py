from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.documents import router as documents_router
from app.api.llm import router as llm_router
from app.api.chat import router as chat_router

app = FastAPI(
    title="EXAONE RAG Project",
    description="Local LLM based RAG API using EXAONE, Ollama, Elasticsearch, and Python.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "project": "EXAONE RAG Project",
        "status": "running",
        "version": "1.0.0",
    }


app.include_router(health_router)
app.include_router(documents_router)
app.include_router(llm_router)
app.include_router(chat_router)