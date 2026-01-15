# Task 4: Inherit Car → ElectricCar
# Create a new class ElectricCar that inherits Car and prints:
# Electric Car is running silently.

class Car:
    def run(self):
        print("Car is running.")


class ElectricCar(Car):
    def run(self):
        print("Electric Car is running silently.")

c = Car()
e = ElectricCar() 
c.run()       
e.run()
# OP:
# Car is running.
# Electric Car is running silently.