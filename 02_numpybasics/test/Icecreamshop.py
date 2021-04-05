import os
import numpy as np


menu = np.array([
  [2,10],
  [3,10],
  [4,10],
  [5,10],
])
name = np.array(["Strewberry","Chocilate", "Vanila", "Orange"])
feature = np.array(["Price", "stock"])

class Shop:
  def __init__(self):
    self.money = 0
  def __del__(self):
    print("Good bye~")
  def icecream_shop(self,sell_icecream,plus_menu,menu_truth,refill):
    running = True
    while running:
      os.system("clear")
      print("                            ")
      print("~~~~~~ICE~~CREAM~~SHOP~~~~~~")
      print("                            ")
      print("Choice Icecream taste       ")
      print("                            ")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~MENU~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("                            ")
      print("1. Strewberry            $2 ")
      print("2. Chocilate             $3 ")
      print("3. Vanila                $4 ")
      print("4. Orange                $5 ")
      print("                            ")
      print("----------------------------")
      print("                            ")
      print("a. Buy Icecream             ")
      print("b. Plus Menu                ")
      print("c. Menu truth               ")
      print("d. Refill                   ")
      print("                            ")
      print("============================")
      choice = input("Choose Alpabet :   ")
      if choice == 'a':
        self.sell_icecream(menu, input("Enter Icecream name: "),money)
      elif choice == 'b':
        plus_menu 
      elif choice == 'c':
        menu_truth
      elif choice == 'd':
        refill
      else:
        running = False
  def menu_data(name_data, feature_data):
    return menu[name == name_data, feature == feature_data]
  def sell_icecream(menu, icecream,money):
    money += menu_data(icecream,"Price")
    menu[name==icecream, feature=="Stock"] -= 1
  def plus_menu(money,name,menu):
    name = np.append(name,input("Plus Icecream name: "))
    menu = np.append(menu, np.array([[5,10]]), axis=0)
  def menu_truth(name,menu):
    truth = name != input("truth menu name: ")
    name = name[truth]
    menu = menu[truth]
  def refill(money):
    stock = menu[:, feature=="Stock"] 
    stock = np.where(stock>5,stock, 10)
      








