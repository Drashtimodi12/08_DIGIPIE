# 25.	Write a Python program to show hierarchical inheritance. 

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