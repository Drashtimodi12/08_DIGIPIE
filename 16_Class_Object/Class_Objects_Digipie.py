# -----------------------------------------
# Example 1: Simple class with class variable
# -----------------------------------------

# Defining a class named 'num'
class num:
    # Class variable (shared by all objects)
    x = 50

# Creating an object of class 'num'
X = num()

# Accessing class variable using object
print(X.x)   # Output: 50

print("\n----------------------------------\n")




# -----------------------------------------
# Example 2: Class with a method that prints value
# -----------------------------------------

# Defining another class named 'Car'
class Car:
    # Class variable
    x = 50

    # Method inside class
    def color(self):
        # 'self.x' is used to access class variable using object
        print(f"Value of x is: {self.x}")

# Creating an object of class 'Car'
A = Car()

# Calling the method using object
A.color()    # Output: Value of x is: 50
