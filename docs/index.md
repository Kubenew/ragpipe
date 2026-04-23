# ragpipe-lite

A lightweight RAG ingestion pipeline toolkit.

## Features

- Text chunking with overlap
- Basic loaders (text files, URLs)
- Embedding generation
- Vector store export

## Quick Start

```bash
pip install ragpipe-lite
```

```python
from ragpipe import Pipeline

p = Pipeline()
p.load("document.txt")
p.chunk()
p.embed()
```