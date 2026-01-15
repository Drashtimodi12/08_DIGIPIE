# Create a class BankAccount with a private attribute balance. 
# Add methods deposit(amount) and get_balance() to update and return the balance. 
# Try to access balance directly from outside and see what happens.

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        a = amount + self.__balance
        self.__balance = a
        print(f"Amount deposited: {amount} Rupees.")
        print(f"Current balance: {self.__balance} Rupees.")

    def get_balance(self):
        return self.__balance
    

b = BankAccount(1000)
b.deposit(200)
print("Balance using getter:", b.get_balance())
# OP:
# Amount deposited: 200 Rupees.
# Current balance: 1200 Rupees.
# Balance using getter: 1200