class BankAccount:
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
                self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()

savings = BankAccount(0.5,1000000)
checking = BankAccount(.02,5000000)

savings.deposit(20).deposit(20).deposit(40).withdraw(800).yield_interest().display_account_info()
checking.deposit(200).deposit(200).deposit(400).withdraw(100).yield_interest().display_account_info()

BankAccount.print_all_accounts()


# User Class

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.balance += amount
        return self
    
    def make_withdrawal(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insuffiecient Funds: Charging a $5 fee")
            self.balance -= 5
            return self
    def display_user_balance(self):
        print(f"Balance: {self.balance}")
        return self
    def example_method(self):
        self.account.deposit(100)
        print(self.account.balance)
