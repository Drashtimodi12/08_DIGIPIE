# Types of Methods in a Class:- 
# 1. Instance Method (display, test)	
# Works with instance attributes (self.id, self.name). Requires an object to call.
# 2. Class Method (show)	
# Works with the class attribute (cls.clg). Can be called on the class itself.
# 3. Static Method (run)	
# Independent of both class and instance. Used for general utility functions.


# Define a class named 'Pen'
class Pen :  

    # Class Attribute (Shared by all instances)
    clg = "drstc"

    # **Constructor (Instance Method)**
    # Initializes instance attributes when an object is created.
    def __init__(self, id, name) :
        self.id = id      # Instance attribute: id
        self.name = name  # Instance attribute: name

    # **Instance Method**
    # Can access and modify object-specific attributes.
    def display(self) :
        print("Display Calling...", self.id, self.name, self.clg)

    # **Class Method**
    # Works with the class variable instead of instance variables.
    # Uses `@classmethod` decorator.
    @classmethod
    def show(cls) :
        print("Show Calling...", cls.clg)

    # **Static Method**
    # Does not use 'self' or 'cls' (i.e., does not access instance or class attributes).
    # Used for utility functions.
    @staticmethod
    def run() :
        print("Run Calling...")

# Updating the class variable before creating objects
Pen.clg = "abc"

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

# OP:
# Display Calling... 10 Akash abc
# Display Calling... 20 Farukh abc
# Display Calling... 30 Rudra abc
# Show Calling... abc
# Run Calling...