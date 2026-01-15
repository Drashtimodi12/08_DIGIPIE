# Animal Sounds (Method Overriding)
# Requirements
# Create a class Animal with method sound().
# Create classes Dog and Cat that override sound().
# Create objects of Dog and Cat and call the method.

class Animal:
    def sound(self):
        print("All animal sound differents...")

class Dog(Animal):
    def sound(self):
        print("Woof Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow Meow!")

obj = Dog(), Cat()

for i in obj:
    i.sound()
# OP:
# Woof Woof!
# Meow Meow!