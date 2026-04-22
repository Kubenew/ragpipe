from ragpipe import ingest_text

data = ingest_text("hello world " * 500)
print("chunks:", len(data["chunks"]))
print("vector_dim:", len(data["vectors"][0]))
