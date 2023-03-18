import requests

url = "http://localhost:8000"

# START SESSION
try:
    response = requests.get(f"{url}/api/start_session")
    session_id = response.json()["sessionId"]
except Exception as e:
    print(e)
    
# USER 1 JOIN SESSION
try:
    response = requests.get(f"{url}/api/join_session?sessionId={session_id}&username=Dawid")    
except Exception as e:
    print(e)


# USER 2 JOIN SESSION
try:
    response = requests.get(f"{url}/api/join_session?sessionId={session_id}&username=John")
except Exception as e:
    print(e)

# SESSION INFO
try:
    response = requests.get(f"{url}/api/session_info?sessionId={session_id}")
except Exception as e:
    print(e)
