class Seller:
    def __init__(self):
        self.money = 0
        self.icecream = 100
    def sell(self):
        self.icecream -= 1
        self.money += 1
    def clean(self):
        print("I sill clean it~")
        self.icecream =+ 1

class Consumer:
    def __init__(self):
        self.money = 100
        self.icecream = 0
    def buy(self):
        self.money -= 1
        self.icecream += 1
    def eat(self):
        self.icecream -= 1
        print("It was delicious!")

class Store:
    def __init__(self):
        self.seonghoon = Seller()
        self.haneun = Conwumer()
    def buy_and_sell(self):
        self.haeun.buy()
        self.seonghoon.sell()
    def eat_and_clean(self):
        self.haneun.eat()
        self.seonghoon.clean()
    def print_status(self):
        running = True
        while running:
            print("wel ")


if __name__ == "__main__":
    store = Store()
    store.buy_and_sell()
    store.eat_and_clean()

