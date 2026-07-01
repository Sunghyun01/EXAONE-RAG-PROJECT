from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ollama_service import generate_answer

router = APIRouter(prefix="/llm", tags=["LLM"])


class LlmTestRequest(BaseModel):
    prompt: str


@router.post("/test")
def test_llm(request: LlmTestRequest):
    return generate_answer(request.prompt)