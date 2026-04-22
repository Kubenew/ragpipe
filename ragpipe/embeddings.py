from typing import List
import numpy as np


class DummyEmbedder:
    """
    Placeholder embedder for v0.1.0.
    Produces deterministic embeddings based on hash.
    """

    def __init__(self, dim: int = 384):
        self.dim = dim

    def embed(self, texts: List[str]) -> np.ndarray:
        vectors = []
        for t in texts:
            h = abs(hash(t)) % 10_000_000
            vec = np.zeros(self.dim, dtype=np.float32)
            vec[h % self.dim] = 1.0
            vectors.append(vec)
        return np.vstack(vectors)
