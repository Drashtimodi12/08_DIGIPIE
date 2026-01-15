"""
Destructor in Python (__del__)
A destructor is a special dunder method that is automatically called when an object is deleted or program ends.
It is used to perform cleanup work like closing files, disconnecting database, releasing memory, etc.


"""

class Demo:
    # Constructor
    def __init__(self, name):
        self.name = name
        print(f"Object created for {self.name}")

    # Destructor
    def __del__(self):
        # This method runs automatically when object is deleted
        print(f"Object destroyed for {self.name}")


# Creating object
obj = Demo("Drashti")

# Deleting object manually
del obj

print("Program End")
# OP:
# Object created for Drashti
# Object destroyed for Drashti
# Program End