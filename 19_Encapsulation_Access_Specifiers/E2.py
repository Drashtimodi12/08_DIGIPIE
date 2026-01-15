# Bank Account With Private Balance
# Requirements
# Create a class BankAccount.
# Private variables:
# __account_number,
# __balance
# Methods:
# deposit(amount) → add money
# withdraw(amount) → deduct money if balance is enough
# get_balance() → return current balance
# Ensure invalid amount (negative or zero) is rejected.
# Use encapsulation to hide sensitive data.

class BankAccount:

    def __init__(self, acc_num, balance):
        self.__acc_num = acc_num        # private attribute
        self.__balance = balance        # private attribute
        
    def deposit(self):
        a = float(input("\nEnter amount to deposit in your account: "))
        if a > 0:
            self.__balance += a
            print(f"Your current balance is : {self.__balance}")
        else:
            print("Invalid amount! Deposit must be greater than 0.")

    def withdraw(self):
        amount = float(input("\nEnter amount to withdraw in your account: "))

        if amount <= 0:
            print("Invalid amount! Withdrawal must be greater than 0.")
        elif amount > self.__balance:
            print("Insufficient balance! Cannot withdraw.")
        else:
            self.__balance -= amount
            print(f"Withdraw: {amount}")
            print(f"Remaining Balance: {self.__balance}")

    def get_balance(self):
        return self.__balance
    

acc1 = BankAccount(12345, 5000)

print(acc1.deposit())
print(acc1.withdraw())
print(f"\nFinal balance is: {acc1.get_balance()}")

# OP:
# Enter amount to deposit in your account: 200
# Your current balance is : 5200.0
# None

# Enter amount to withdraw in your account: 200
# Withdraw: 200.0
# Remaining Balance: 5000.0
# None

# Final balance is: 5000.0