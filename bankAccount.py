class BankAccount:
    def __init__(self, account_type, balance):
        self.balance = balance
        self.type = account_type

    def __str__(self):
        return f"{self.type}: ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

