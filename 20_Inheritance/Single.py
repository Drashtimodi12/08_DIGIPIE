"""
Inheritance is an OOP concept where a child class inherits attributes and methods 
from a parent class. This helps in code reusability and modularity.

Python supports 5 types of inheritance:
    1. Single Inheritance
    2. Multiple Inheritance
    3. Multilevel Inheritance
    4. Hierarchical Inheritance
    5. Hybrid Inheritance

"""

"""
Single Inheritance  
One parent → One child  
Example: Parent → Child  
Child inherits methods of Parent
"""

# Parent class
class Animal:
    # Parent class method
    def sound(self):
        print("Animals make some sound")

# Child class inheriting from Animal
class Dog(Animal):   
    # Child class own method
    def bark(self):
        print("Dog barks")

# Creating object of child class
obj = Dog()

# Calling parent's method using child object
obj.sound()   # Dog gets this method from Animal (inherited)

# Calling child's own method
obj.bark()    # This method belongs to Dog class only
# OP:
# Animals make some sound
# Dog barks




print("\n==================================\n")




# A child class inherits from a single parent class.

# Parent class
class Animal :
    def speak(self) :
        print("Animal Speaks.")


# Child class inheriting from Animal
class Dog(Animal) :
    def Bark(self) :
        print("Dog Barks.")

# Creating an object of the Dog class
dog = Dog()
dog.speak()     # Inherited method from Animal
dog.Bark()      # Own method

# Output:
# Animal Speaks.
# Dog Barks.