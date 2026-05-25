from fastapi import APIRouter
from backend.app.models.schema import (
    MeetingInput,
    SentimentInput,
    QuestionInput
)

from backend.app.ml.sentiment import get_sentiment
from backend.app.genai.summarizer import summarize_text
from backend.app.genai.actions import extract_actions
from backend.app.rag.qa import ask_question

router = APIRouter()

MEETINGS = {}

@router.get("/test")
def test():
    return {"message": "API working"}

@router.post("/ingest")
def ingest(data: MeetingInput):

    if data.meeting_id not in MEETINGS:
        MEETINGS[data.meeting_id] = []

    MEETINGS[data.meeting_id].append(data.text)

    return {
        "message": "Meeting ingested",
        "meeting_id": data.meeting_id
    }

@router.get("/meeting/{meeting_id}")
def get_meeting(meeting_id: str):

    transcripts = MEETINGS.get(meeting_id, [])

    return {
        "meeting_id": meeting_id,
        "transcripts": transcripts
    }

@router.post("/sentiment")
def sentiment(data: SentimentInput):

    score = get_sentiment(data.text)

    return {
        "sentiment": score
    }

@router.get("/summary/{meeting_id}")
def summary(meeting_id: str):

    text = " ".join(
        MEETINGS.get(meeting_id, [])
    )

    summary = summarize_text(text)

    return {
        "summary": summary
    }

@router.get("/actions/{meeting_id}")
def actions(meeting_id: str):

    text = " ".join(
        MEETINGS.get(meeting_id, [])
    )

    actions = extract_actions(text)

    return {
        "actions": actions
    }

@router.post("/ask")
def ask(data: QuestionInput):

    answer = ask_question(data.query)

    return {
        "answer": answer
    }