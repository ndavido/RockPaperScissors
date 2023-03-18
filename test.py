import requests

url = "http://localhost:8000"

# START SESSION
response = requests.get(f"{url}/api/start_session")
session_id = response.json()["sessionId"]
print(response.json())

# USER 1 JOIN SESSION
response = requests.get(f"{url}/api/join_session?sessionId={session_id}&username=Dawid")
assert response.status_code == 200, "Failed to join session"
assert response.json()["status"] == 1, "Failed to join session"

# USER 2 JOIN SESSION
response = requests.get(f"{url}/api/join_session?sessionId={session_id}&username=John")
assert response.status_code == 200, "Failed to join session"
assert response.json()["status"] == 1, "Failed to join session"

# SESSION INFO
response = requests.get(f"{url}/api/session_info?sessionId={session_id}")
assert response.status_code == 200, "Failed to get session info"
print(response.json())
