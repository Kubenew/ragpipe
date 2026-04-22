from ragpipe import chunk_text


def test_chunking():
    chunks = chunk_text("a" * 1000, chunk_size=200, overlap=50)
    assert len(chunks) > 0
