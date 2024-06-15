class Customer:
    accounts = []
    savings_withdraw_count = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name + "Accounts: " + str(self.accounts)

    def add_account(self, new_account):
        self.accounts.insert(0, new_account)

    def close_account(self, account_index):
        self.accounts.pop(account_index)

    def debit_account(self, account_index, amount):
        if account_index not in self.accounts:
            print("Invalid account index")
            return False
        self.accounts[account_index].deposit()
        return True

    def credit_account(self, account_index, amount):
        if account_index not in self.accounts:
            print("Invalid account index")
            return False
        if self.accounts[account_index].balance() < amount:
            print("Insufficient funds")
            return False
        self.accounts[account_index].withdraw(amount)
        if self.accounts[account_index].type == "Savings":
            self.savings_withdraw_count += 1

    def list_accounts(self):
        print(f"Accounts for {self.name}:")
        for i in range(len(self.accounts)):
            print(i, ". ", str(self.accounts[i]))
