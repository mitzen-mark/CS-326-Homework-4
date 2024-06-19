class Customer:

    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.savings_withdraw_count = 0

    def __str__(self):
        return self.name

    def add_account(self, new_account):
        self.accounts.insert(0, new_account)

    def close_account(self, account_index):
        self.accounts.pop(account_index)

    def debit_account(self, account_index, amount):
        if account_index < 0 or account_index >= len(self.accounts):
            print("Invalid account index")
            return False
        self.accounts[account_index].deposit(amount)
        return True

    def credit_account(self, account_index, amount):
        if account_index < 0 or account_index >= len(self.accounts):
            print("Invalid account index")
            return False
        if self.accounts[account_index].balance() < amount:
            print("Insufficient funds")
            return False
        self.accounts[account_index].withdraw(amount)
        if self.accounts[account_index].type == "Savings":
            self.savings_withdraw_count += 1
            print(f"New balance: {self.accounts[account_index].balance()}")
        if self.savings_withdraw_count >= 6:
            self.savings_deduction(self, account_index)

    def list_accounts(self):
        print(f"Accounts for {self.name}:")
        for i in range(len(self.accounts)):
            print(i, ". ", str(self.accounts[i]))

    def savings_deduction(self, account_ind):
        self.accounts[account_ind].withdraw(10)
        self.savings_withdraw_count = 0
        if self.accounts[account_ind].balance < 0:
            print("Account closure or something lol")
            return False
        return True
