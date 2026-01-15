# Vehicle Abstraction
# Requirements:
# Create an abstract class Vehicle with abstract method start().
# Create two child classes: Car and Bike.
# Implement start() in each child class.
# Add a concrete method stop() in the abstract class and use it in child classes.

from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod     # If we not use decorator then code becomes normal inheritance, not abstraction.
    def start(self):
        pass

    def stop(self):
        print("Stopped Vehicle.")

class Car(Vehicle):
    def start(self):
        print("\nCar has started with a key ignition.")

class Bike(Vehicle):
    def start(self):
        print("\nBike has started with self-start button.")


C = Car()
C.start()
C.stop()
# OP:
# Car has started with a key ignition.
# Stopped Vehicle.


B = Bike()
B.start()
B.stop()

# OP:
# Bike has started with self-start button.
# Stopped Vehicle.