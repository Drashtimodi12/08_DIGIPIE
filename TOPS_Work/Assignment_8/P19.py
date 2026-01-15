# 19.	Write a Python program to create a class and access the properties of the class using an object. 

# Define a class named 'Pen'
class Pen :

    # Method to display class attributes
    def display(self) :
        print("Display Calling...")

    # Another method inside the class
    def test(self) :
        print("Test Calling...")

# Creating objects of class 'Pen'
P = Pen()       # Creating an instance (object) of the 'Pen' class
P.display()     # Calling the 'display' method using the object 'P'
P.test()        # Calling the 'test' method using the object 'P'

# Output:
# Display Calling...
# Test Calling...
