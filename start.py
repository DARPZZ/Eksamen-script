import brugere
import requests
import ipadresser
import adminlogin
 
import time
def main():
   brugere.init_emails()
   brugere.set_first_name()
   brugere.set_second_name()
   brugere.ct()
   brugere.init_emails()
   
   with requests.Session() as session:
      adminlogin.login(session)
      ipadresser.create_ips(session)
      brugere.assing_drawer_to_user(session)
      
   
   
if __name__ == "__main__":
    main()