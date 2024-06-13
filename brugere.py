import random
import csv
from passwordgenerator import pwgenerator
import requests
from concurrent.futures import ThreadPoolExecutor
import adminlogin
first_name = []
last_name = []
full_name = ""
all_names=[]

user_emails = []



def init_emails():
    global user_emails
    for user_info in all_names:
        email_address = user_info['email']
        user_emails.append(email_address)

def assing_drawer_to_user(session):
    
    i = 2
    for email in user_emails:
        
        payload = {
            "email": email,
            "id" : i
        }
        
        response = session.post("http://127.0.0.1:4000/locks/user/", json=payload)

        if response.status_code == 201 or response.status_code == 200:
            
            print(f"User created successfully: {payload}")

        else:
            print(f"Failed to create user: {response.status_code} - {response.text}")
        i = i+1
        

        
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
            

def random_number(min_val,max_val):
    return random.randint(min_val, max_val - 1)


def set_password():
   return pwgenerator.generate()

def create_user():
  
    global all_names
    først_navn = first_name[random_number(0,len(first_name))]
    andet_navn = last_name[random_number(0,len(last_name))]
    email = (først_navn + andet_navn + "@gmail.com").lower()
   
    password = set_password()
    payload = {
        "email": email,
        "password": password,
        "firstName": først_navn,
        "lastName": andet_navn,
        
    }

    response = requests.post("http://127.0.0.1:4000/users", json=payload)
    
    if response.status_code == 201:
        print(f"User created successfully: {payload}")
        all_names.append(payload)
        
        
        
    else:
        print(f"Failed to create user: {response.status_code} - {response.text}")
        




def create_specific_user():
  
    
    først_navn = "Bob"
    andet_navn = "Hansen"
    email = (først_navn + andet_navn + "@gmail.com").lower()
   
    password = set_password()
    payload = {
        "email": email,
        "password": password,
        "firstName": først_navn,
        "lastName": andet_navn,
        
    }

    response = requests.post("http://127.0.0.1:4000/users", json=payload)
    
    if response.status_code == 201:
        print(f"User created successfully: {payload}")
        
        
        
        
    else:
        print(f"Failed to create user: {response.status_code} - {response.text}")
        
        
        


def assing_drawer_to_specific_user(session):
        
        payload = {
            "email": "bobhansen@gmail.com",
            "id" : 1
        }
        
        response = session.post("http://127.0.0.1:4000/locks/user/", json=payload)

        if response.status_code == 201 or response.status_code == 200:
            print(f"User created successfully: {payload}")

        else:
            print(f"Failed to create user: {response.status_code} - {response.text}")
       
        
        
    
    
    
    
    
def ct():
    for _ in range(100):
        create_user()
