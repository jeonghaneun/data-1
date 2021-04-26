import os
import numpy as np



class Shop:
  def __init__(self):
    self.menu = np.array([
      [2,10],
      [3,10],
      [4,10],
      [5,10],
      ])
    self.name = np.array(["Strewberry","Chocolate", "Vanila", "Orange"])
    self.feature = np.array(["Price", "Stock"])
    self.money = 0
  def __del__(self):
    print("Good bye~")
  def icecream_shop(self):
    running = True
    while running:
      os.system("clear")
      print("                            ")
      print("~~~~~~ICE~~CREAM~~SHOP~~~~~~")
      print(f"${self.money}              ")
      print("                            ")
      print("Choice Icecream taste       ")
      print("                            ")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~MENU~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("                            ")
      self.print_icecream()
      print("                            ")
      print("----------------------------")
      print("                            ")
      print("a. Buy Icecream             ")
      print("b. Add Menu                ")
      print("c. Remove Menu ")
      print("d. Refill                   ")
      print("                            ")
      print("============================")
      choice = input("Choose Alpabet :   ")
      if choice == 'a':
        self.buy_icecream()
      elif choice == 'b':
        self.add_menu()
      elif choice == 'c':
        self.remove_menu()
      elif choice == 'd':
        self.refill()
      elif choice =='q':
        running = False
      else:
        pass
  def print_icecream(self):
    for index, value in enumerate(self.name):
      print(f"{index+1}. {value}     ${self.menu[index][0]}   Stock:{self.menu[index][1]} ")
  def menu_data(self,name_data,feature_data):
    return self.menu[self.name == name_data, self.feature == feature_data]
  def buy_icecream(self):
    icecream = 0
    running = True
    while running:
      icecream = input("Choose Number :   ")
      if icecream in [str(i) for i in range(1, len(self.name)+1)]:
        icecream = self.name[int(icecream)-1]
        self.money += self.menu_data(icecream,"Price")
        self.menu[self.name==icecream, self.feature=="Stock"] -= 1
        running = False
      else:
        pass
  def add_menu(self):
    self.name = np.append(self.name,input("Add Icecream name: "))
    self.menu = np.append(self.menu, np.array([[int(input("Price : ")),10]]), axis=0)
  def remove_menu(self):
    truth = self.name != input("Remove menu name: ")
    self.name = self.name[truth]
    self.menu = self.menu[truth]
  def refill(self):
    stock = self.menu[:, self.feature=="Stock"] 
    self.menu[:, self.feature=="Stock"]= np.where(stock>5,stock, 10)
      

if __name__=="__main__":
  shop = Shop()
  shop.icecream_shop()






