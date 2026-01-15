# Task 7: Create a class Laptop with:
# class attribute: brand = "Dell"
# constructor for model & price
# method to display all info


class Laptop:
    brand = 'Dell'

    def __init__(self, model, price):
        self.model = model
        self.price = price

    def display(self):
        print(f"My laptop brand is {self.brand} and model name {self.model}, price is something {self.price}.")

L1 = Laptop('Elitebook', 25000)

L1.display()
# OP:
# My laptop brand is Dell and model name Elitebook, price is something 25000.