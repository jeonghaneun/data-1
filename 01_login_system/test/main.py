import os

running = True
money = 0


while running:
  os.system("clear")
  print(f"=========Money:{money}  =====")
  print("=======fjkslfjldkjf===========")
  print("1.can         $12             ")
  print("2.aluminuium  $11             ")
  print("3.can         $09             ")
  print("4.botle       $15             ")
  print("==============================")
  choice = input("Choose Trust: ")
  if choice == '1':
    money = money+12
  elif choice == '2':
    money = money+11
  elif choice == '3':
    money = money+9
  elif choice == '4':
    money = money+15
  elif choice == 'q':
    running = False







  