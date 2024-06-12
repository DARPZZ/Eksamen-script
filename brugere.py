import random
import csv
from passwordgenerator import pwgenerator
import requests
from concurrent.futures import ThreadPoolExecutor
first_name = []
last_name = []
full_name = ""
def set_first_name():
    global first_name  
    with open('fornavnecsv.csv', mode='r', encoding='utf-8') as file:
        csvFile = csv.reader(file, delimiter=';')
        next(csvFile)  
        for lines in csvFile:
            first_element = lines[0]
            first_name.append(first_element)


def set_second_name():
    global last_name  
    with open('efternavnecsv.csv', mode='r', encoding='utf-8') as file:
        for line in file:
            last_name.append(line.strip())
            

def random_number(max_val):
    return random.randint(0, max_val - 1)


def set_password():
   return pwgenerator.generate()

async def create_user():
    
    først_navn = first_name[random_number(len(first_name))]
    andet_navn = last_name[random_number(len(last_name))]
    email = først_navn + andet_navn + "@gmail.com"
    password = set_password()
    payload = {
        "email": email,
        "password": password,
        "firstName": først_navn,
        "lastName": andet_navn
    }

    response = requests.post("http://127.0.0.1:4000/users", json=payload)
    
    if response.status_code == 201:
        print(f"User created successfully: {payload}")
    else:
        print(f"Failed to create user: {response.status_code} - {response.text}")

async def create_users_multithreaded(num_threads):
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for _ in range(100):
            executor.submit(create_user)
   


