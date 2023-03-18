from fastapi import FastAPI
import random

app = FastAPI()

sessions = {}

@app.get("/api/start_session")
async def start_session():
    sessionId = str(random.randint(100000, 999999))
    sessions[sessionId] = {
        "players": {},
        "results": {}
    }
    return {
        "status": 1,
        "message": f"Session {sessionId} was created successfully.",
        "sessionId": sessionId
    }

@app.get("/api/join_session")
async def join_session(sessionId, username):
    return {}