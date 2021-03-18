import os
import time

print("m.druken")

class User:
  def __init__(self):
    self.money = 0 
    self.size = 0
  def __del__(self):
    print("Next")
  def bye_Item(self):
    running
    while running:
      os.system("clear")
      print(f"========Money:{self.money}=========")
      print("==============Itemstore=============")
      print("1. fruit                     $2     ")
      print("2. drinks                    $3     ")
      print("3. medicine                  $4     ")
      print("4. honey                     $5     ")
      choice = input("Choose Item: ")
      if choice == '1':
        self.money = self.money-2
        self.size = self.size-20
      elif choice == '2':
        self.money = self.money-3
        self.size = self.size+30
      elif choice == '3':
        self.money = self.money-5
        self.size = self.size+50
      elif choice == '4':
        self.money = self.money-7
        self.size = self.size+100
      elif choice == 'q':
        running = False
      else:
        pass

class Game:
  def __init__(self):
    self.Liver_size = 0
  def __del__(self):
    print("Next") 
  def GAMESTART(self):
    running = True
    while running:
      os.system("clear")
      print(f"=========   Choice Drink   =========")
      print("====================================")
      print("1. Soju                          ===")
      print("2. Bear                          ===")
      print("3. Whisky                        ===")
      print("4. Rum                           ===")
      print("5. Finished                      ===")
      choice = input("Drinking: ")
      if choice == '1':
        self.Liver_size = self.Liver_size-10
      elif choice == '2':
        self.Liver_size = self.Liver_size-5
      elif choice == '3':
        self.Liver_size = self.Liver_size-20
      elif choice == '4':
        self.Liver_size = self.Liver_size-35
      elif choice == '5':
        running = False
      else:
        pass

class LIVERSIZE:
  def Ending(self,liversize):
    for user in liversize: 
      self.Liver_size >= self.size:
      print("SUCCESS")
    time.sleep(3)
    for user in liversize: 
      self.Liver_size < self.size:
      print("OVERIT!!!!!!!!!!!!!!!!!!")
    time.sleep(3)

  


