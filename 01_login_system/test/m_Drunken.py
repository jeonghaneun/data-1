import os
import time
import m_Item

print("m.druken")

class User:
  def __init__(self):
    self.money = 30 
    self.size = 0
    self.item_dict = m_Item.item_dict
  def __del__(self):
    print("Next")
  # Ending according to liver size
  def ending(self):
    if self.size > 0:
      print(f"SUCCESS! My liver size is {self.size}")
      time.sleep(3)
    elif self.size <= 0:
      print(f"GAME-OVER! My liver size is {self.size}")
      time.sleep(3)
  # Check money
  def check_money(self, choice_money):
    if self.money < choice_money:
      return False
    else:
      return True
  # Buying items to increase liver size (only fruit decreases the liver size)
  def buy_item(self):
    running = True
    while running:
      os.system("clear")
      print(f"========Money:{self.money}=========")
      print("==============Itemstore=============")
      for i in self.item_dict:
        print(f"{i['id']}. {i['item']}           $ {i['price']}   ")
      print("q. exit                             ")
      choice = input("Choose Item: ")
      for i in self.item_dict: 
        if choice == str(i['id']):
          running = self.check_money(i['price'])
          self.money = self.money-i['price']
          self.size = self.size+i['health']
          break
      if choice == 'q':
        running = False
      else:
        pass

class Game:
  def __del__(self):
    print("Next") 
  def game_start(self, user):
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
        user.size = user.size-10
      elif choice == '2':
        user.size = user.size-5
      elif choice == '3':
        user.size = user.size-20
      elif choice == '4':
        user.size = user.size-35
      elif choice == '5':
        running = False
      else:
        pass

if __name__ == "__main__":
  time.sleep(3)
  # 0. Create user and game
  user = User()
  game = Game()
  # 1. user buys item
  user.buy_item()
  # 2. game tries to kill user
  game.game_start(user)
  # 3. ending
  user.ending()

  


