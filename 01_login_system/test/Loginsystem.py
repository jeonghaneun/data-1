import os
import time

class Client:
  def enterInformation(self):
    self.email = input("Enter email:")
    self.password = input("Enter password:")
  def print_yourself(self):
    print(f"Email:{self.email}")
    print(f"Password:{self.password}")
class Admin:
  def printCredentails(self,client_list):
    print ("================Client List=============")
    for client in client_list: 
      client.print_yourself()
    print("=====================================") 
  def login(self,client_list):
    email = input("Type email: ")
    password = input("Type password: ")
    for client in client_list: 
      if email is client.email and password is client.password:
        print ("Login succeeded")
        time.sleep(2)
      else:
        print ("Login Failed") 
        time.sleep(2)

client_list = []
admin = Admin()
running =True
while running:
  os.system("clear")
  admin.printCredentails(client_list)
  print ("================Select=============")
  print ("A. Create Email ane Password")
  print ("B. Log in")
  print ("Q. Quit")
  selectKey = input("Choose onr: ")
  if selectKey == 'a':
    client = Client()
    client.enterInformation()
    client_list.append(client)
  elif selectKey == 'b':
    admin.login(client_list)
  elif selectKey == 'q':
    running = False
  else:
    pass  
