from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_service import ask_rag

router = APIRouter(prefix="/chat", tags=["Chat"])


class ChatRequest(BaseModel):
    question: str
    size: int = 5


@router.post("")
def chat(request: ChatRequest):
    return ask_rag(
        question=request.question,
        size=request.size,
    )