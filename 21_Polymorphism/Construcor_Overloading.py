# Constructor Overloading in Python:- Constructor overloading is a concept in object-oriented programming where a class 
# can have multiple constructors (methods of the same name but with different parameters). However, Python does not 
# support constructor overloading directly like some other languages (e.g., C++ or Java). In Python, you can achieve 
# similar functionality by using default arguments or variable-length arguments (*args or **kwargs) in a single constructor. 
# Instead, we can achieve it using:

# 1. Default arguments
# 2. Variable-length arguments (*args)
# 3. Conditional logic in the __init__ method

# Constructor Overloading using Variable-Length Arguments (*args)

class Sample:
    def __init__(self, *a):
        # """ Constructor with variable-length arguments to simulate overloading """
        self.a = a[0]
        self.b = a[1]

    def desp(self):
        # """ Method to display the values of a and b """
        print(self.a, self.b)

class Demo(Sample):
    def __init__(self, a, b, c):
        # """ Child class constructor calls Parent's constructor using super() """
        super().__init__(10, 20, 30)  # Parent constructor called with three arguments

# Creating object of Demo class
d = Demo(10, 20, 30)

# Calling desp() method to print values
d.desp()

# Output: 10 20




print("\n---------------------------------------\n")


# Demonstrating Constructor Overloading and Inheritance in Python
# Parent class
class Sample:

    # Constructor accepting variable number of arguments using *args
    def __init__(self, *a):
        if len(a) == 2:  # Ensuring at least two arguments are passed
            self.a = a[0]
            self.b = a[1]
        else:
            raise ValueError("Constructor requires exactly two arguments")

    # Method to display values
    def desp(self):
        print(self.a, self.b)

# Child class inheriting from Sample
class Demo(Sample):

    def __init__(self, a, b, c):
        # Correcting the super() call to pass only two arguments (matching parent class constructor)
        super().__init__(a, b)  # Calling the parent class constructor correctly
        self.c = c  # Additional attribute in child class

    def desp(self):
        # Overriding the desp() method to include the third attribute
        print(self.a, self.b, self.c)

# Creating an object of Demo class
d = Demo(10, 20, 30)
d.desp()  
# OP: 10 20 30