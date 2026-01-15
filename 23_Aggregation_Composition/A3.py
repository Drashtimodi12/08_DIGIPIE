# Task 3: Add a new class Driver
# Create a Driver class with a method drive(car) that calls car.run().
# Example:
# d = Driver()
# d.drive(c)

class Driver:
    def drive(self, car):
        print("Driver drive the car.")
        car.run()

class Car:
    def run(self):
        print("Car is runing.")

d = Driver()
c = Car()
d.drive(c)
# OP:
# Driver drive the car.
# Car is runing.