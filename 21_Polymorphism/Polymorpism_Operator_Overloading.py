"""
Operator Polymorphism: Operator Polymorphism means the same operator behaves differently 
    based on the type of data it is used with.      Same operator, multiple forms = polymorphism.

Example:
5 + 10 → performs addition
"A" + "B" → performs string join (concatenation)
[1, 2] + [3, 4] → performs list merge

Because of this flexible behavior, Python supports polymorphism with operators.
"""



# Integer addition
a = 10
b = 20
print("Integer addition:", a + b)

# String concatenation
s1 = "Hello "
s2 = "World"
print("String concatenation:", s1 + s2)

# List joining
l1 = [1, 2, 3]
l2 = [4, 5]
print("List joining:", l1 + l2)
# OP:
# Integer addition: 30
# String concatenation: Hello World
# List joining: [1, 2, 3, 4, 5]







print("\n=============================\n")





# Operator Overloading Example in Python
# This code demonstrates operator overloading in Python by defining a class with custom behavior for the addition 

class Demo:
    def __init__(self, a, b):
        # Initialize the instance with values a and b
        self.a = a
        self.b = b
    
    def __add__(self, obj):
        # Overload the addition operator
        # Return a tuple with the sum of a and b from both objects
        return self.a + obj.a, self.b + obj.b

    def __mul__(self, obj):
        # Overload the multiplication operator
        # Return a tuple with the product of a and b from both objects
        return self.a * obj.a, self.b * obj.b

# Create two instances of the Demo class
d1 = Demo(10, 20)
d2 = Demo(20, 40)

# Use the overloaded multiplication operator
c = d1 * d2

# Print the result
print(c)  
# Output: (200, 800)'