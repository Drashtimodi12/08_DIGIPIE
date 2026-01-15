# Demonstrating the use of inheritance and the `super()` function in Python

# Parent class
class P:

    def __init__(self):
        print("Class P constructor calling")  # Constructor of class P

# Child class inheriting from P
class Q(P):

    def __init__(self):
        print("Class Q constructor calling")  # Constructor of class Q
        super().__init__()  # Calling the parent class constructor using super()


# Creating an object of class Q
q = Q()  

# Output:
# Class Q constructor calling
# Class P constructor calling