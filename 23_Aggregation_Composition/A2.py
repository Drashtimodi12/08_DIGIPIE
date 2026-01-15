# Task 2: Add fuel check
# Inside Engine, create a variable fuel and check:
# If fuel > 0 → print “Engine Started”
# Else → print “No fuel! Please fill.”

class Engine:
    def __init__(self, fuel):
        self.Fuel = fuel

    def check_fuel(self):
        if self.Fuel > 0 :
            print("Engine Started.")
        else:
            print("No fuel! Please fill.")

class Car:
    def __init__(self, engine):
        self.engine = engine
    def run(self):
        print("Car is trying to start..")
        self.engine.check_fuel()

e = Engine(23)
c = Car(e)
c.run()
# OP:
# Car is trying to start..
# Engine Started.