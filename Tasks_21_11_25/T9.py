# Create a class Pen with attributes color and price. 
# Create three pen objects with different colors and prices, and print their details.

class Pen:

    def __init__(self, color, price):
        self.color = color
        self.price = price

p1 = Pen('Red', 2.5)
print(f"I have {p1.color} color Pen priced at {p1.price}.")

p2 = Pen('Blue', 5)
print(f"I have {p2.color} color Pen priced at {p2.price}.")

p3 = Pen('Black', 1)
print(f"I have {p3.color} color Pen priced at {p3.price}.")

# OP:
# I have Red color Pen priced at 2.5.
# I have Blue color Pen priced at 5.
# I have Black color Pen priced at 1.