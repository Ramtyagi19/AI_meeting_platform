from fastapi import FastAPI
from backend.app.api.routes import router

app = FastAPI(
    title="AI Meeting Platform"
)

app.include_router(router)

@app.get("/")
def home():
    return {"status": "running"}