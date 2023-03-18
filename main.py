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
            "message": f"Cannot join a session. User with the name {username} has already joined the session."
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
        
@app.get("/api/session_info")
async def session_info(sessionId: str):
    if sessionId not in sessions:
        return {
            "status": 0,
            "message": "Session with this ID does not exist."
        }
    else:
        session_data = sessions[sessionId]
        if len(session_data["players"]) < 2:
            return {
                "status": 1,
                "message": f"Session {sessionId} has been created but has not started yet.",
                "sessionId": sessionId
            }
        else:
            player1, player2 = session_data["players"].keys()
            outcome1, outcome2 = session_data["players"].values()
            winner = determine_winner(outcome1, outcome2)
            session_data["results"]["player1"] = outcome1
            session_data["results"]["player2"] = outcome2
            session_data["results"]["winner"] = winner
            return {
                "status": 1,
                "message": f"Session {sessionId} has been completed successfully.",
                "sessionId": sessionId,
                "player1": player1,
                "player2": player2,
                "outcome1": outcome1,
                "outcome2": outcome2,
                "winner": winner
            }

def determine_winner(outcome1: str, outcome2: str) -> str:
    if outcome1 == outcome2:
        return "tie"
    elif (outcome1 == "rock" and outcome2 == "scissors") or (outcome1 == "paper" and outcome2 == "rock") or (outcome1 == "scissors" and outcome2 == "paper"):
        return "player1"
    else:
        return "player2"