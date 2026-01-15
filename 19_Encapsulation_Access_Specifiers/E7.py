# Car Speed Encapsulation
# Requirements
# Class Car
# Private:
# __speed
# Methods:
# set_speed() → must be between 0 and 300
# accelerate(value) → add value
# brake(value) → reduce speed
# get_speed()

class Car:

    def __init__(self):
        self.__speed = 90

    def get_speed(self):
        return self.__speed

    def set_speed(self):
        current_speed = int(input("Enter your car speed: "))

        if 0 <= current_speed <= 300 :
            self.__speed = current_speed
            print(f"Speed set to {self.__speed} km/h")
        else:
            print("Invalid! Speed must be between 0 and 300.")

    def accelerate(self):
        accelerate_speed = int(input("\nEnter your car accelerate speed: "))
        new_speed = self.__speed + accelerate_speed
        if new_speed <= 300:
            self.__speed = new_speed
            print(f"Car accelerated. Current speed: {self.__speed} km/h")
        else:
            print("Cannot exceed 300 km/h speed limit!")

    def brake(self):
        brake_value = int(input("\nEnter your car brake value: "))
        brake_speed = self.__speed - brake_value
        if brake_speed >= 0 :
            self.__speed = brake_speed
            print(f"Car slowed down. Current speed: {self.__speed} km/h")
        else:
            self.__speed = 0 
            print("Car stopped. Speed is now 0 km/h.\n")

c1 = Car()
c1.set_speed()
c1.accelerate()
c1.brake()
c1.get_speed()
# op:
# Enter your car speed: 100
# Speed set to 100 km/h

# Enter your car accelerate speed: 10
# Car accelerated. Current speed: 110 km/h

# Enter your car brake value: 0
# Car slowed down. Current speed: 110 km/h