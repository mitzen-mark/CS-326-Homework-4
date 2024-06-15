from customer import Customer
from bankAccount import BankAccount

print("Hello World")
james = Customer("James")
account = BankAccount("Checking", 12.50)
james.add_account(account)
james.list_accounts()
