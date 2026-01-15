# Encapsulation is the concept of hiding the internal details of a class and restricting direct access to some 
# attributes using private (__), protected (_), and public variables.


# Define a class named BankAccount
class BankAccount :

    def __init__(self, acc_num, balance) :
        self.acc_num = acc_num          # Public attribute
        self.__balance = balance        # Private attribute (Encapsulation)

    # Public method to check balance
    def get_balance(self) :
        return self.__balance
    
    # Public method to deposit money
    def deposit(self, amount) :
        if amount > 0 :
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else :
            print("Invalid deposite ammount.")

    # Public method to withdraw money
    def withdraw(self, amount) :
        if self.__balance >= amount > 0 :
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else :
            print("Insufficient balance or invalid amount.")

        
# Creating an object of BankAccount class
num1 = BankAccount(1001, 5000)

# Accessing public attribute
print(f"Account Number: {num1.acc_num}")

# Using getter method to access balance
print(f"Current Balance: {num1.get_balance()}")

# Accessing private attribute (will cause an error)
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# Using getter method to access balance
num1.get_balance()

# Performing transactions
num1.deposit(2000)
num1.withdraw(8000)

# Checking balance after transactions
print("Updated Balance:", num1.get_balance())


# Output:
# Account Number: 1001
# Current Balance: 5000
# ₹2000 deposited successfully.
# Insufficient balance or invalid amount.
# Updated Balance: 7000