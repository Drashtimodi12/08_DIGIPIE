# Vehicle Inheritance System – Hierarchical Inheritance
# Requirements:
# Create class Vehicle
# method: start()
# Create class Car(Vehicle)
# method: wheels() → print number of wheels
# Create class Bike(Vehicle)
# method: wheels()
# Create objects & demonstrate hierarchical inheritance.


class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def wheels(self):
        print("A car has 4 wheels.")

class Bike(Vehicle):
    def wheels(self):
        print("A bike has 2 wheels.")

c = Car()
c.start()
c.wheels()
# OP:
# Vehicle is starting...
# A car has 4 wheels.

b = Bike()
b.start()
b.wheels()
# OP:
# Vehicle is starting...
# A bike has 2 wheels.