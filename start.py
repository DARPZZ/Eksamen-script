import brugere
import requests
import ipadresser
import adminlogin
def main():
   brugere.set_first_name()
   brugere.set_second_name()
   brugere.create_users_multithreaded(5)
   with requests.Session() as session:
      adminlogin.login(session)
      ipadresser.create_ip_multithreaded(session,5)
   
if __name__ == "__main__":
    main()