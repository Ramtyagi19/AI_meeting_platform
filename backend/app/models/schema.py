from pydantic import BaseModel

class MeetingInput(BaseModel):
    meeting_id: str
    text: str

class SentimentInput(BaseModel):
    text: str

class QuestionInput(BaseModel):
    query: str