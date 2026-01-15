# Vehicle Start (Different Classes, Same Method)
# Requirements
# Classes: Car, Bike, Bus
# All should have a method start().
# Loop through all objects and call start().

class Car:
    def start(self):
        print("Car have 4 wheels")

class Bike:
    def start(self):
        print("Car have 2 wheels")

class Bus:
    def start(self):
        print("Car have 6 wheels")

c = Car()
b = Bike()
bu = Bus()

for obj in (c, b, bu):
    obj.start()
# OP:
# Car have 4 wheels
# Car have 2 wheels
# Car have 6 wheels