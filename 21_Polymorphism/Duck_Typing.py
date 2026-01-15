"""
Duck Typing means Python does not care about the class of an object. 
It only cares whether the object has the required methods.
    “If it walks like a duck and quacks like a duck, treat it like a duck.”

If two objects have the same method, Python allows them to be used in the same way, 
even if they belong to different classes.

Why Duck Typing is Polymorphism?
    Because it allows same function to work with different types of objects based on behavior (methods), not on class.
    Ex: display() works with Duck, Dog, Cat (if Cat also had speak method).
"""

# Duck class with swim() and speak() methods
class Duck:
    def swim(self):
        print("I am Duck and I am swimming.")
    def speak(self):
        print("Duck Duck!")

# Dog class with swim() and speak() methods
class Dog:
    def swim(self):
        print("I am Dog and I am swimming.")
    def speak(self):
        print("Woof Woof!")

# Cat class (only has swim, no speak method)
class Cat:
    def swim(self):
        print("I am Cat and I am swimming.")

# Function that accepts any object
# It only expects the object to have swim() and speak() methods
def display(*args):
    for obj in args: 
        obj.swim()    # Calls the object's swim() method
        obj.speak()   # Calls the object's speak() method
        print("Information Displayed...\n")

# Creating objects of each class
duck = Duck()
dog = Dog()
cat = Cat()

# Passing different objects to display() function
display(duck, dog)
display(cat)    # This will cause ERROR because Cat has no speak() method

# OP:
# I am Duck and I am swimming.
# Duck Duck!
# Information Displayed...

# I am Dog and I am swimming.
# Woof Woof!
# Information Displayed...

# I am Cat and I am swimming.
