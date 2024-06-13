import requests
from Ip import IP
from random_ip_generator import random_ip_for_country
from concurrent.futures import ThreadPoolExecutor
list_af_ips =[]
def create_new_ip():
    country_code = "DK"
    random_ip = random_ip_for_country(country_code)
   
    return random_ip
def create_IP(session):
    global list_af_ips
    ip =create_new_ip()
    payload = {
        "ip": str(ip),
    }
    response = session.post(f"http://{IP}:4000/locks", json=payload)
    print(response.status_code)
    if response.status_code == 201:
        print(f"User created successfully: {payload}")
        list_af_ips.append(payload)
    else:
        print(f"Failed to create user: {response.status_code} - {response.text}")


def create_specific_IP(session):
    payload = {
        "ip": "10.176.69.22",
    }
    response = session.post(f"http://{IP}:4000/locks", json=payload)
    print(response.status_code)
    if response.status_code == 201:
        print(f"User created successfully: {payload}")
        
    else:
        print(f"Failed to create user: {response.status_code} - {response.text}")
        
def create_ips(session):
    for _ in range(200):
        create_IP(session)