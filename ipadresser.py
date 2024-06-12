import requests
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
    response = session.post("http://127.0.0.1:4000/locks", json=payload)
    print(response.status_code)
    if response.status_code == 201:
        print(f"User created successfully: {payload}")
        list_af_ips.append(payload)
    else:
        print(f"Failed to create user: {response.status_code} - {response.text}")
        
def create_ip_multithreaded(session, num_threads):
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for _ in range(200):
            executor.submit(create_IP, session)