class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, type, balance=0):
        self.savings_account = 0
        self.checking_account = 0
        if type == "savings":
            self.savings_account = balance
        if type == "checking":
            self.checking_account = balance
        self.interest_rate = int_rate * .01
        BankAccount.all_accounts.append(self)

    def deposit(self, type, amount):
        if type == "savings":
            self.savings_account += amount
        if type == "checking":
            self.checking_account += amount
        return self
    
    def withdrawl(self, type, amount):
        if type == "savings":
            if self.savings_account < 0:
                print("Insufficient funds: Charging a $5 fee")
                self.savings_account -= 5
            else:    
                self.savings_account -= amount
            return self
        if type == "checking":
            if self.checking_account < 0:
                print("Insufficient funds: Charging a $5 fee")
                self.checking_account -= 5
            else:    
                self.savings_account -= amount
            return self

    def display_account_info(self, type):
        if type == "savings":
            print(f"Savings Balance: ${self.savings_account}")
            return self
        if type == "checking":
            print(f"Checking Balance: ${self.checking_account}")
            return self
        if type == "accounts":
            accounts = self.savings_account + self.checking_account
            print(f"Checking Balance: ${self.checking_account}")
            print(f"Savings Balance: ${self.savings_account}")
            print(f"Accounts Balance: ${accounts}")
            return self


    def yield_interest(self):
        if self.savings_account > 0:
            interest_return = self.savings_account * self.interest_rate
            self.savings_account += interest_return
            self.savings_account = round(self.savings_account, 2)
            return self
        if self.checking_account > 0:
            interest_return = self.checking_account * self.interest_rate
            self.checking_account += interest_return
            self.checking_account = round(self.checking_account, 2)
            return self


class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate=0.00, type="" , balance=0)

    def make_withdrawal(self, type, amount):
        self.account.withdrawl(type, amount)
        return self

    def display_user_balance(self, type):
        print(self.account.display_account_info(type))
        return self

    def make_deposit(self, type, amount):
        self.account.deposit(type, amount) 
        return self

    def make_transfer(self, amount, to_whom):
        self.account_balance -= amount
        print(f"{self.name} transferred ${amount} to {to_whom.name}.")
        to_whom.account_balance += amount
        print(f"{to_whom.name} received ${amount} from {self.name}.")

p1 = User("John")
p2 = User("Lilly")

p1.make_deposit("savings", 1500)
p1.make_deposit("checking", 2459)
p1.display_user_balance("accounts")

p2.make_deposit("savings", 46528.95)
p2.make_withdrawal("savings", 965.35)
p2.make_deposit("checking", 94632.55)
p2.make_withdrawal("checking", 762.45)
p2.display_user_balance("accounts")


