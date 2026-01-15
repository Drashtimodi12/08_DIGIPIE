# Create a class Animal with a method sound() that prints "Some sound". Create a subclass Dog that 
# overrides sound() to print "Woof".


class Animal:
    def sound(self):
        print("Animal different sounds....")

class Dog(Animal):
    def sound(self):
        print("Woof Woof!")

a = Animal()
a.sound()

d = Dog()
d.sound()

# OP:
# Animal different sounds....
# Woof Woof!
