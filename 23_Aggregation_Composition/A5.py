# Task 5: Add speed functionality
# Inside the Car class:
# Create a variable speed
# Add a method accelerate() that increases speed by 10
# Print current speed


class Car:
    def __init__(self):
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        print("Current speed: ", self.speed )

c = Car()
c.accelerate()
c.accelerate()
c.accelerate()
# OP:
# Current speed:  10
# Current speed:  20
# Current speed:  30


