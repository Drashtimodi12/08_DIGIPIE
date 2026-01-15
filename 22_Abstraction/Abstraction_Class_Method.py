from abc import ABC, abstractmethod

class Account(ABC):

    balance = 0  # Default balance for all accounts

    @abstractmethod
    def deposit(self, amount):
        pass  # Abstract method (Must be implemented by child classes)

    def checkBalance(self):
        print("Current balance is:", self.balance)

# Saving Account (Child Class)
class SavingAccount(Account):

    def deposit(self, amt):
        self.balance += amt  # Deposits money in the account

# Loan Account (Child Class)
class LoanAccount(Account):

    def deposit(self, amount):
        self.balance -= amount  # Deducts loan repayment amount from balance

# Creating a Saving Account object
s = SavingAccount()
s.checkBalance()  # Initially 0
s.deposit(5000)
s.deposit(8000)
s.checkBalance()  # Updated Balance

print("*********************")

# Creating a Loan Account object
l = LoanAccount()
l.balance = 10000  # Setting initial loan amount
l.checkBalance()
l.deposit(5000)  # Repaying loan
l.checkBalance()  # Updated Loan Balance



# Output:
# Current balance is: 0
# Current balance is: 13000
# *********************
# Current balance is: 10000
# Current balance is: 5000