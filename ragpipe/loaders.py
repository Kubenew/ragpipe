import os
import requests


def load_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def load_directory(path: str) -> dict:
    docs = {}
    for root, _, files in os.walk(path):
        for fn in files:
            if fn.lower().endswith((".txt", ".md")):
                full = os.path.join(root, fn)
                docs[full] = load_text_file(full)
    return docs


def load_url(url: str, timeout: int = 15) -> str:
    r = requests.get(url, timeout=timeout)
    r.raise_for_status()
    return r.text
