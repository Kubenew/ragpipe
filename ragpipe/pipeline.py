from typing import Dict, Any
from .chunking import chunk_text
from .loaders import load_text_file, load_url
from .embeddings import DummyEmbedder


def ingest_text(text: str, source: str = "text", chunk_size: int = 500, overlap: int = 50) -> Dict[str, Any]:
    chunks = chunk_text(text, chunk_size=chunk_size, overlap=overlap)
    embedder = DummyEmbedder()
    vectors = embedder.embed(chunks)

    return {
        "source": source,
        "chunk_size": chunk_size,
        "overlap": overlap,
        "chunks": chunks,
        "vectors": vectors.tolist(),
    }


def ingest_file(path: str, chunk_size: int = 500, overlap: int = 50) -> Dict[str, Any]:
    text = load_text_file(path)
    return ingest_text(text, source=path, chunk_size=chunk_size, overlap=overlap)


def ingest_url(url: str, chunk_size: int = 500, overlap: int = 50) -> Dict[str, Any]:
    text = load_url(url)
    return ingest_text(text, source=url, chunk_size=chunk_size, overlap=overlap)
