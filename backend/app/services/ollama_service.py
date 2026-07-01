import os
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "exaone3.5:7.8b")


def generate_answer(prompt: str) -> dict:
    url = f"{OLLAMA_URL}/api/generate"

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(url, json=payload, timeout=120)
    response.raise_for_status()

    data = response.json()

    return {
        "model": data.get("model", OLLAMA_MODEL),
        "answer": data.get("response", ""),
        "done": data.get("done"),
        "total_duration": data.get("total_duration"),
        "eval_count": data.get("eval_count"),
    }