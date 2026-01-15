# Class with class attribute
class Employee:

    # Class attribute (same for all objects)
    company = "Google"

    def __init__(self, name, salary):
        self.name = name      # Instance attribute
        self.salary = salary  # Instance attribute

# Creating objects
e1 = Employee("Riya", 40000)
e2 = Employee("Jay", 50000)

# Accessing class and instance attributes
print(e1.name, e1.salary, e1.company)  # Riya 40000 Google
print(e2.name, e2.salary, e2.company)  # Jay 50000 Google

print("\n---------------------------\n")


# Task 2
# Create a class Car with an attribute brand.
# Create an object and print:

class Car:
    # Class attribute
    brand = 'Hyundai'

    def __init__(self):
        print(f"This car i20 car brand is: {self.brand}")

c1 = Car()
# OP: This car i20 car brand is: Hyundai