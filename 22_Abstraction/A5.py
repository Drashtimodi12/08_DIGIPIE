# Abstraction with Concrete + Abstract Methods
# Requirements:
# Abstract class Appliance:
# Abstract method: turn_on()
# Concrete method: turn_off() → prints "Appliance is off"
# Child class: Fan → implement turn_on()
# Create object and test both methods.

from abc import ABC, abstractmethod

class Appliance(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    def turn_off(self):
        print("Appliance is off.")

class Fan(Appliance):
    def turn_on(self):
        print("Fan is on.")

f = Fan()
f.turn_on()
f.turn_off()
# OP:
# Fan is on.
# Appliance is off.