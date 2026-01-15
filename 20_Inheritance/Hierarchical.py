"""
Hierarchical Inheritance  
One parent → multiple children  
Example: Vehicle → (Car, Bike)
All children inherit from the same parent class
"""

# Parent class
class vehical:
    # Common method for all vehicles
    def start(self):
        print("\nVehical Starts.")

# Child class 1 → inherits from vehical
class car(vehical):
    # Method specific to car
    def car_info(self):
        print("Red color car.")

# Child class 2 → inherits from vehical
class Bike(vehical):
    # Method specific to bike
    def bike_info(self):
        print("2 wheel bike.")

# Creating object of Car class
c = car()
c.start()        # Using parent class method
c.car_info()     # Using child class method

# Creating object of Bike class
b = Bike()
b.start()        # Using parent class method
b.bike_info()    # Using child class method
# OP:
# Vehical Starts.
# Red color car.

# Vehical Starts.
# 2 wheel bike.


print("\n==================================\n")

# Multiple child classes inherit from the same parent class.

# Parent class
class vehical :
    def fuel(self) :
        print("Vehical use fuel.")

# Child class 1 inheriting from Vehicle
class car(vehical) :
    def wheels(self) :
        print("Car has 4 wheels.")

# Child class 2 inheriting from Vehicle
class bike(vehical) :
    def wheels(self) :
        print("Bike has 2 wheels.")

# Creating objects of both child classes
c = car()
b = bike()

c.fuel()   # Inherited method
c.wheels() # Car's method

b.fuel()   # Inherited method
b.wheels() # Bike's method

# Output:
# Vehical use fuel.
# Car has 4 wheels.
# Vehical use fuel.
# Bike has 2 wheels.