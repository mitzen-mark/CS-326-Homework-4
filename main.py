from customer import Customer
from bankAccount import BankAccount


def main():
    james = Customer("James")
    charlie = Customer("Charlie")
    jenny = Customer("Jenny")
    cassandra = Customer("Cassandra")
    checking1 = BankAccount("Checking", 12.50)
    checking2 = BankAccount("Checking", 5600)
    checking3 = BankAccount("Checking", 0)
    checking4 = BankAccount("Checking", 89.23)
    savings1 = BankAccount("Savings", 300)
    savings2 = BankAccount("Savings", 900000)
    savings3 = BankAccount("Savings", 20)
    savings4 = BankAccount("Savings", 6356.27)

    james.add_account(checking1)
    james.add_account(savings1)
    jenny.add_account(checking2)
    jenny.add_account(savings2)
    charlie.add_account(checking3)
    charlie.add_account(savings3)
    cassandra.add_account(checking4)
    cassandra.add_account(savings4)

    customer_list = [james, charlie, jenny, cassandra]

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 0:
                print("Closing program")
                break
            elif choice == 1:
                customer_lookup(customer_list)
            else:
                print("Invalid choice. Please enter 0 or 1.")
        except ValueError:
            print("Invalid choice. Please enter 0 or 1.")


def display_menu():
    print("The Bank™ Accounting Program")
    print("1. Search for a Customer")
    print("0. Exit")


def customer_lookup(customer_registry):
    choice = (input("Enter customer name: "))
    found_customer = next((customer for customer in customer_registry if customer.name == choice), None)
    if found_customer:
        print("Customer found")
        found_customer.list_accounts()
        while choice != 0:
            print("Enter an option listed below:")
            print("1. Debit Account")
            print("2. Credit Account")
            print("0. Return to Main Menu")
            choice = int(input())
            if choice == 1 or choice == 2:
                account_ind = int(input("Enter account number to modify: "))
                account_modification(found_customer, choice, account_ind)
                choice = 0
            if choice == 0:
                return
            else:
                print("Invalid choice")

    else:
        print("Customer not found")


def account_modification(customer, previous_choice, index):
    if previous_choice == 1:
        debit_amount = int(input("Enter debit amount: "))
        customer.debit_account(index, debit_amount)
    if previous_choice == 2:
        credit_amount = int(input("Enter credit amount: "))
        customer.credit_account(index, credit_amount)


if __name__ == "__main__":
    main()
