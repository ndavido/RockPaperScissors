from fastapi import FastAPI

app = FastAPI()

@app.get("/api/start_session")
async def start_session():
    return {}

@app.get("/api/join_session")
async def join_session(sessionId, username):
    return {}