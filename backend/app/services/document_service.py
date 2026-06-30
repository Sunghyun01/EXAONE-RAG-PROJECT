from pathlib import Path

def read_text_file(file_path: str)-> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return path.read_text(encoding="utf-8")

def split_text_to_chunks(text: str, chunk_size: int = 300, overlap: int = 50)-> list[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start = end - overlap

    return chunks