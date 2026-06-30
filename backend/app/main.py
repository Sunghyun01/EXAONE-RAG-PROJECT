from fastapi import FastAPI
from app.api.health import router as health_router

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