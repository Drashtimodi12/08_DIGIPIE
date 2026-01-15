# __str__(self): This special (dunder) method controls what gets printed
# when you directly print an object of the class.
# Without __str__, Python prints the memory address of the object.

class string:
    
    # Constructor - initializes object with 'name'
    def __init__(self, name):
        self.name = name   # Instance variable storing the name

    # __str__ is used to return a human-readable string representation of the object.
    # Whenever print(object) is used, Python internally calls object.__str__().
    def __str__(self):
        return f"My name is {self.name}."

# Creating an object of the class
s = string('Drashti')

# When we print the object 's', __str__ method automatically executes
print(s)        # OP: My name is Drashti.
# If you removed the __str__ method:   <__main__.string object at 0x0000025F5B3>