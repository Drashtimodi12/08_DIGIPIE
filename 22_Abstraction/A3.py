# Payment System
# Requirements:
# Abstract class Payment:
# Abstract method: pay(amount)
# Child classes: CreditCard and PayPal
# Implement pay() differently for each payment type.
# Create objects and show payment messages.

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"\nPaid ₹{amount} using Credit Card.")


class PayPal(Payment):
    def pay(self, amount):
        print(f"\nPaid ₹{amount} using PayPal.")

cc = CreditCard()
cc.pay(1000)
# OP: Paid ₹1000 using Credit Card.


pp= PayPal()
pp.pay(2000)
# OP: Paid ₹2000 using PayPal.