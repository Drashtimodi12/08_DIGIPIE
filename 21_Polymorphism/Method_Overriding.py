# Method overriding occurs when a child class (subclass) provides a specific implementation of a method that 
# is already defined in its parent class (superclass).

# In simple words:- Same method name in both parent and child classes.
# Child class modifies or changes the behavior of the parent class method.



class A:
    def disp(self):
        print("Class A disp method calling")

class B(A):
    def disp(self):
        print("Class B disp method calling")

# Create an instance of class B
b = B()
# Call the disp method
b.disp()

# Output:
# Class B disp method calling


print("\n------------------------------------------\n")

# Parent class
class Animal:
    def speak(self):
        print("Animal is speaking")

# Child class
class Dog(Animal):
    def speak(self):
        print("Dog is barking")

# Create object of Dog
d = Dog()
d.speak()  # Output: Dog is barking