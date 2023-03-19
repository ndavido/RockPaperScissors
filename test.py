import requests

url = "http://localhost:8000"

# START SESSION
print('\n----------------\nSTART SESSION\n----------------')
try:
    response = requests.get(f"{url}/api/start_session")
    session_id = response.json()["sessionId"]
    print(response.json())
except Exception as e:
    print(e)
    
# USER 1 JOIN SESSION
print('\n----------------\nUSER 1 JOIN SESSION\n----------------')
try:
    response = requests.get(f"{url}/api/join_session?sessionId={session_id}&username=Dawid")   
    print(response.json()) 
except Exception as e:
    print(e)

# TRY TO SEE SESSION INFO
print('\n----------------\nTRY TO SEE SESSION INFO\n----------------')
try:
    response = requests.get(f"{url}/api/session_info?sessionId={session_id}")
    print(response.json())
except Exception as e:
    print(e)

# USER 2 WITH SAME NAME AS USER 1 JOIN SESSION
print('\n----------------\nUSER 2 WITH SAME NAME AS USER 1 JOIN SESSION\n----------------')
try:
    response = requests.get(f"{url}/api/join_session?sessionId={session_id}&username=Dawid")
    print(response.json())
except Exception as e:
    print(e)

# USER 2 JOIN SESSION
print('\n----------------\nUSER 2 JOIN SESSION\n----------------')
try:
    response = requests.get(f"{url}/api/join_session?sessionId={session_id}&username=John")
    print(response.json())
except Exception as e:
    print(e)
    
# USER 2 JOIN SESSION
print('\n----------------\nUSER 3 JOIN SESSION\n----------------')
try:
    response = requests.get(f"{url}/api/join_session?sessionId={session_id}&username=Mark")
    print(response.json())
except Exception as e:
    print(e)

# USER 2 JOINING A SESSION THAT DOES NOT EXIST
print('\n----------------\nUSER 2 JOINING A SESSION THAT DOES NOT EXIST\n----------------')
try:
    response = requests.get(f"{url}/api/join_session?sessionId=1234567890&username=John")
    print(response.json())
except Exception as e:
    print(e)

# SESSION INFO - INVALID SESSION ID
print('\n----------------\nSESSION INFO - INVALID SESSION ID\n----------------')
try:
    response = requests.get(f"{url}/api/session_info?sessionId=1234567890")
    print(response.json())
except Exception as e:
    print(e)

# SESSION INFO
print('\n----------------\nSESSION INFO\n----------------')
try:
    response = requests.get(f"{url}/api/session_info?sessionId={session_id}")
    print(response.json())
except Exception as e:
    print(e)

