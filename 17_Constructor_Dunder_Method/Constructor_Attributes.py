# Types of Attributes in a Class:- 
# 1. Instance Attributes (Defined inside __init__ using self)
# Specific to each object (instance).
# Example: self.id, self.name

# 2. Class Attributes (Defined at the class level, shared among all objects)
# Common for all instances of the class.
# Example: clg = "drstc"

# 3. Static Attributes (Accessed using static methods, but not related to any instance or class)
# Used when the function logic does not rely on instance or class variables.
# Example: @staticmethod


# Define a class named 'Pen'
class Pen:  

    # **Class Attribute** (Shared by all instances)
    clg = "drstc"

    # **Instance Attributes**
    # Constructor (Instance Method)- Initializes instance attributes when an object is created.
    def __init__(self, id, name):
        self.id = id      # Instance attribute: id
        self.name = name  # Instance attribute: name

    # Instance Method- Can access and modify object-specific attributes.
    def display(self):
        print("Display Calling...", self.id, self.name, self.clg)

    # Instance Method- Another example of an instance method.
    def test(self):
        print("Test Calling...")

    # Class Method- Works with the class variable instead of instance variables.
    # - Uses `@classmethod` decorator.
    @classmethod
    def show(cls):
        print("Show Calling...", cls.clg)

    # Static Method- Does not use 'self' or 'cls' (i.e., does not access instance or class attributes).
    # - Used for utility functions.
    @staticmethod
    def run():
        print("Run Calling...")


# Updating the class variable before creating objects
Pen.clg = "GPG"

# Creating objects (instances) of the class 'Pen'
p = Pen(10, "Akash")
p.display()  # Calls instance method

p1 = Pen(20, "Farukh")
p1.display()

p2 = Pen(30, "Rudra")
p2.display()

# Calling class method (does not require an instance)
Pen.show()

# Calling static method (does not require an instance)
Pen.run()

# Output:
# Display Calling... 10 Akash GPG
# Display Calling... 20 Farukh GPG
# Display Calling... 30 Rudra GPG
# Show Calling... GPG
# Run Calling...