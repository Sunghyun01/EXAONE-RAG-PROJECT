from fastapi import APIRouter
from app.services.elastic_service import check_elasticsearch_health

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("")
def health_check():
    return {
        "status": "ok",
        "message": "EXAONE RAG Backend is running",
    }


@router.get("/elasticsearch")
def elasticsearch_health_check():
    return check_elasticsearch_health()