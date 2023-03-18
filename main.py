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
async def join_session(sessionId: str, username: str):
    if sessionId not in sessions:
        return {
            "status": 0,
            "message": "Cannot join a session. Session with this ID does not exist."
        }
    elif len(sessions[sessionId]["players"]) >= 2:
        return {
            "status": 0,
            "message": "Cannot join a session. Session already has two players."
        }
    elif username in sessions[sessionId]["players"]:
        return {
            "status": 0,
            "message": f"Cannot join a session. {username} has already joined the session."
        }
    else:
        outcome = random.choice(["rock", "paper", "scissors"])
        sessions[sessionId]["players"][username] = outcome
        return {
            "status": 1,
            "message": f"{username} joined session {sessionId} successfully.",
            "sessionId": sessionId,
            "username": username
        }