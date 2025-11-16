# Define a class for a Bank Account
class BankAccount:
    # Constructor to initialize account details
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive!")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Withdrawal amount must be positive!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

    # Method to display account info
    def display_account(self):
        print(f"Account holder: {self.account_holder}, Balance: ${self.balance}")

# Create objects for two accounts
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

print("\n")
# Interact with the accounts
account1.display_account()
account1.deposit(200)
account1.withdraw(150)

account2.display_account()
account2.deposit(300)
account2.withdraw(1000) 