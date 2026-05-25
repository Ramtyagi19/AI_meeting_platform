from backend.app.genai.summarizer import summarize_text
from backend.app.genai.actions import extract_actions

def test_summary():

    text = """
    Kafka lag issue discussed.
    Deployment failure discussed.
    """

    summary = summarize_text(text)

    assert summary is not None
    assert len(summary) > 0

def test_actions():

    text = """
    Ram should fix Kafka issue.
    DevOps should validate cluster.
    """

    actions = extract_actions(text)

    assert len(actions) > 0