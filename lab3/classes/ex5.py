class Account:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def deposit(self, money):
        self.balance+=money
        print(f"Количество баланса: {self.balance}")

    def withdraw(self,money):
        if 0<money<=self.balance:
            self.balance-=money
            print(f"Снято {money} денег")
            print(f"Количество баланса: {self.balance}")

        else:
            print("Недостаточно денег на балансе")

acc=Account((input()), int(input()))
acc.deposit(1000)
acc.withdraw(500)