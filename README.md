# ragpipe-lite

[![PyPI Version](https://img.shields.io/pypi/v/ragpipe-lite)](https://pypi.org/project/ragpipe-lite/)
[![Python Versions](https://img.shields.io/pypi/pyversions/ragpipe-lite)](https://pypi.org/project/ragpipe-lite/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/Kubenew/ragpipe/actions/workflows/ci.yml/badge.svg)](https://github.com/Kubenew/ragpipe/actions/workflows/ci.yml)
[![Downloads](https://pepy.tech/badge/ragpipe-lite)](https://pepy.tech/project/ragpipe-lite)

`ragpipe` is a lightweight RAG ingestion pipeline toolkit.

It helps you go from documents → chunks → embeddings → vector store export.

## Features (v0.1.0)

- text chunking with overlap
- basic loaders (text files, URLs)
- embedding interface abstraction
- JSON export format
- optional FAISS dependency group

## Install

```bash
pip install ragpipe
```

Optional FAISS:

```bash
pip install ragpipe[faiss]
```

## CLI usage

```bash
ragpipe ingest ./docs --out out.json
ragpipe ingest-url https://example.com --out out.json
```

## Python usage

```python
from ragpipe import chunk_text, ingest_text

chunks = chunk_text("hello world " * 200, chunk_size=200, overlap=50)
print(len(chunks))

data = ingest_text("hello world " * 200)
print(data.keys())
```

## License
MIT
