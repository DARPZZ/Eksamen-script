import brugere
import requests
import ipadresser
import adminlogin

from concurrent.futures import ThreadPoolExecutor

def main():
    brugere.set_first_name()
    brugere.set_second_name()
    
       
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.submit(brugere.create_users_multithreaded, 10)
        with requests.Session() as session:
            adminlogin.login(session)
            executor.submit(ipadresser.create_ip_multithreaded, session, 10)
   

if __name__ == "__main__":
   main()
  