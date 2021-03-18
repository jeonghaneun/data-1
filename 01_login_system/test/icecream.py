import os

class Owner:
  #Construcdor
  def __init__(self):
    self.money = 0
  #Destructor
  def __del__(self):
    print("Jangsa is over")
  #Methode
  def sell_Icecream(self): 
    running = True
    while running:
      os.system("clear")
      print(f"=========Money:{self.money}  =====")
      print("=======IcecreamHi+++===========")
      print("1.strewberry  $12             ")
      print("2.choco       $11             ")
      print("3.banana      $09             ")
      print("4.blueberry   $15             ")
      print("==============================")
      choice = input("Choose Icecream: ")
      if choice == '1':
        self.money = self.money+12
      elif choice == '2':
        self.money = self.money+11
      elif choice == '3':
        self.money = self.money+9
      elif choice == '4':
        self.money = self.money+15
      elif choice == 'q':
        running = False
      else:
        pass

owner = Owner()
owner.sell_Icecream()

