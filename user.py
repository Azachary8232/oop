class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_withdrawal(self,amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(self.name, self.account_balance)

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_transfer(self, amount, to_whom):
        self.account_balance -= amount
        print(f"{self.name} transferred ${amount} to {to_whom.name}.")
        to_whom.account_balance += amount
        print(f"{to_whom.name} received ${amount} from {self.name}.")

p1 = User("John")
p2 = User("Mark")
p3 = User("Mary")

p1.make_deposit(250)
p1.make_deposit(745)
p1.make_deposit(1025.65)
p1.make_deposit(62.47)
p1.display_user_balance()

p2.make_deposit(8521.65)
p2.make_deposit(45)
p2.make_withdrawal(651)
p2.make_withdrawal(219.25)
p2.display_user_balance()

p3.make_deposit(455)
p3.make_withdrawal(212.25)
p3.make_withdrawal(168.96)
p3.make_withdrawal(201.10)
p3.display_user_balance()

p1.make_transfer(500,p3)
p1.display_user_balance()
p3.display_user_balance()