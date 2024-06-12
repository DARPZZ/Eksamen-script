import brugere
import ipadresser
import adminlogin
import requests
def main():
   brugere.set_first_name()
   brugere.set_second_name()
   # brugere.create_users_multithreaded(5)
   with requests.Session() as session:
      adminlogin.login(session)
      ipadresser.create_IP(session)
     
   
   
if __name__ == "__main__":
    main()

