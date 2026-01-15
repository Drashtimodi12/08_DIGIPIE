"""
What is Aggregation in Python (OOP)?
    Aggregation means one class has another class as a PART of it, 
    both can exist independently.
    Object created outside
    It is also called a “Weak HAS-A relationship.”

Examples in real life:
    A School has Students (but students can exist without school)
    A Company has Employees (but employees can exist without company)
Objects are connected
But they don’t depend on each other for survival
If the main object is deleted, the contained object still lives
"""
class Engine:
    # A simple class with one method
    def start(self):
        print("Engine Started.")


# Car does NOT inherit Engine now — it only USES Engine
class Car:
    # Constructor receives an Engine object
    def __init__(self, engine):
        # engine comes from outside, Car Weak HAS-A Engine (Aggregation)
        self.engine = engine   # making object of parent class

    def run(self):
        print("Car is running.")
        # Using Engine method through the object
        self.engine.start()     # object throug calling function of parent class


# Creating Engine object separately
e = Engine()

# Passing engine object into Car (Aggregation)
c = Car(e)

# Running the car (Engine is used inside Car)
c.run()
# OP:
# Car is running.
# Engine Started.


"""
✔ Key Checks:
Object created outside → yes (e = Engine())
Passed into another class → yes (Car(e))
Weak HAS-A → correct
Both objects independent → correct

Comments clearly explain:
✔ Engine exists separately
✔ Car only uses Engine
✔ Deleting Car will not delete Engine
"""