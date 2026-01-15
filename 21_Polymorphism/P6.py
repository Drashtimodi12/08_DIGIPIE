# Employee Work (Same Method in Different Classes)
# Requirements
# Create class Developer → method work() → prints "Writes code"
# Create class Designer → method work() → prints "Creates UI"
# Create class Tester → method work() → prints "Tests software"
# Call work() for every object in a loop.

class Developer:
    def work(self):
        print("Writes Code")

class Designer:
    def work(self):
        print("Creates UI")

class Tester:
    def work(self):
        print("Tests software")

employees = [Developer(), Designer(), Tester()]

for emp in employees:
    emp.work()
# OP:
# Writes Code
# Creates UI
# Tests software