from backend.app.ml.sentiment import get_sentiment
from backend.app.ml.topic_clustering import cluster_topics

def test_sentiment():

    text = "This meeting was excellent"

    score = get_sentiment(text)

    assert score > 0

def test_clustering():

    texts = [
        "Kafka deployment issue",
        "Databricks streaming",
        "Team lunch discussion"
    ]

    labels = cluster_topics(texts)

    assert len(labels) == 3