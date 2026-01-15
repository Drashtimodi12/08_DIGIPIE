# Task 9: Create a class BankAccount with:
# attributes: name, balance
# methods: deposit(), withdraw(), check_balance()
# Simulate transactions using objects.

class BankAccount:
    
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
            print(f"\nDeposite amount is {amount} and Total Balance is {self.balance}")
        else:
            print("\nDeposite amount is must be Positive.")


    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"\nWithdrw amount is {amount} and total Balance is {self.balance}")
            else:
                print("\nInsufficient Balance.")
        else:
            print("\nDeposite amount is must be Positive.")

    def check_balance(self):
        print(f"\nOwner name is {self.name}. \nCurrent Balance is {self.balance} Rupess.")

acc1 = BankAccount('Drashti', 1000)
acc2 = BankAccount('Sejal', 5050)

acc1.deposit(10)
acc1.check_balance()
acc1.withdraw(700)
acc1.check_balance()
print('-------------------------------')
acc2.check_balance()
acc2.withdraw(30)
acc2.deposit(100)
acc2.check_balance()

# OP:

# Deposite amount is 10 and Total Balance is 1010

# Owner name is Drashti.
# Current Balance is 1010 Rupess.

# Withdrw amount is 700 and total Balance is 310

# Owner name is Drashti.
# Current Balance is 310 Rupess.
# -------------------------------

# Owner name is Sejal.
# Current Balance is 5050 Rupess.

# Withdrw amount is 30 and total Balance is 5020

# Deposite amount is 100 and Total Balance is 5120

# Owner name is Sejal.
# Current Balance is 5120 Rupess.