class BankAccount:
    #balance_of_all_accounts = 0
    all_accounts = []

    def __init__(self, int_rate, balance=0):
        self.account_balance = balance
        self.interest_rate = int_rate * .01
        BankAccount.all_accounts.append(self)
    #    BankAccount.balance_of_all_accounts += balance

    def deposit(self, amount):
        self.account_balance += amount
    #    BankAccount.balance_of_all_accounts += amount
        return self
    
    def withdrawl(self, amount):
        if self.account_balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        else:    
            self.account_balance -= amount
        #    BankAccount.balance_of_all_accounts -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.account_balance}")
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            interest_return = self.account_balance * self.interest_rate
            self.account_balance += interest_return
            self.account_balance = round(self.account_balance, 2)
        #    BankAccount.balance_of_all_accounts += interest_return
        #    BankAccount.balance_of_all_accounts = round(BankAccount.balance_of_all_accounts,2)
        return self

    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += all_accounts.account_balance
        return sum

checking_account = BankAccount(4, 10500)
savings_account = BankAccount(1.5, 750)


checking_account.deposit(500).deposit(1000).deposit(5000).withdrawl(2000).yield_interest().display_account_info()
savings_account.deposit(621.56).deposit(45.14).withdrawl(74.10).withdrawl(.12).withdrawl(112.25).withdrawl(62.77).yield_interest().display_account_info()

print(all_balances())