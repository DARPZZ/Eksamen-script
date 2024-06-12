import requests

def login(session):
    payload = {
        "email": "admin@mail.com",
        "password": "admin"
    }
    response = session.post("http://127.0.0.1:4000/admin/signin", json=payload)
    
    if response.status_code == 200:
        print(f"Admin login: {payload}")
    else:
        print(f"Failed to create user: {response.status_code} - {response.text}")


