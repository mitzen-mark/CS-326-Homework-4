from customer import Customer
from bankAccount import BankAccount

print("Hello World")
james = Customer("James")
charlie = Customer("Charlie")
jenny = Customer("Jenny")
cassandra = Customer("Cassandra")
checking1 = BankAccount("Checking", 12.50)
checking2 = BankAccount("Checking", 5600)
checking3 = BankAccount("Checking", 0)
savings1 = BankAccount("Savings", 300)
savings2 = BankAccount("Savings", 900000)
savings3 = BankAccount("Savings", 20)

james.add_account(checking1)
james.add_account(savings1)
jenny.add_account(checking2)

james.list_accounts()
