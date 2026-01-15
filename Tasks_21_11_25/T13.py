# Create a class Engine with a method start(). Create a class Car that has an Engine object and 
# a method drive() which first starts the engine, then prints "Car is moving".

class Engine:
    def start(self):
        print("Engine Starts.")

class Car(Engine):
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is moving.")

c = Car()
c.drive()
# OP:
# Engine Starts.
# Car is moving.