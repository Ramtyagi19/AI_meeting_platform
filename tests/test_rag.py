from backend.app.rag.vector_store import (
    store_embedding,
    search_similar
)

def test_vector_store():

    store_embedding(
        "1",
        "Kafka deployment pipeline"
    )

    results = search_similar(
        "deployment issue"
    )

    assert results is not None