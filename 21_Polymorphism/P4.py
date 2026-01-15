# Method Overriding in Multilevel Inheritance
# Requirements
# Class Device → method power()
# Class Laptop(Device) → override power()
# Class GamingLaptop(Laptop) → override again
# Create object of GamingLaptop and call power().

class Device:
    def power(self):
        print("HP Device...")

class Laptop(Device):
    def power(self):
        print("I5 Laptop...")

class GamingLaptop(Laptop):
    def power(self):
        print("Gaming Laptop requires high power for graphics.")

obj = GamingLaptop()
obj.power()
# OP:
# Gaming Laptop requires high power for graphics.