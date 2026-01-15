# Class with instance attributes
class Student:
    def __init__(self, name, marks):
        # Instance attributes (different for each object)
        self.name = name
        self.marks = marks

# Creating objects
s1 = Student("Drashti", 90)
s2 = Student("Prince", 85)

# Accessing instance attributes
print(s1.name, s1.marks)   # Output: Drashti 90
print(s2.name, s2.marks)   # Output: Prince 85

print("\n-----------------------------\n")



# Task 1:- Create a class Student with attributes:
# name
# roll_no
# Create 2 objects and print their details.
# Define a class Student

class Student:

    # Constructor that assigns instance attributes
    def __init__(self, name, roll_no):
        self.name = name       # Instance Attribute
        self.roll_no = roll_no # Instance Attribute

# Creating two Student objects
s1 = Student('Drashti', 1)
s2 = Student('Sejal', 2)

# Printing details of each student
print("Name:", s1.name, " Roll No:", s1.roll_no)        # OP: Name: Drashti  Roll No: 1
print("Name:", s2.name, " Roll No:", s2.roll_no)        # OP: Name: Sejal  Roll No: 2
print("\n-----------------------------\n")



# Task 3
# Create a class Mobile with a constructor that sets price and model.
# Create an object and print both values.

class Mobile:

    # Constructor to set price and model
    def __init__(self, price, model):
        self.price = price     # Instance attribute
        self.model = model     # Instance attribute

    # Method to print the details
    def fun(self):
        print(f"Mobile price is {self.price} and model is {self.model}")

# Creating object
m = Mobile(10000, 'A51')

# Printing values
m.fun()
# OP: Mobile price is 10000 and model is A51