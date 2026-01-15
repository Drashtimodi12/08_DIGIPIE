# In the previous example, make Dog call the sound() method of Animal using super().

class Animal:
    def sound(self):
        print("All animals different sounds...")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Woof Woof!")

d = Dog()
d.sound()
# OP:
# All animals different sounds...
# Woof Woof!