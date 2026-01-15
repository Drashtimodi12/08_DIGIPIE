# 18.	Write a Python program to create a class and access its properties using an object. 

# Define a class named Car
class Car :

    # Class-level property
    brand = "Toyoto"

    # Constructor to initialize properties
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
# Create an object of the Car class
c = Car("Corolla", 2022)

# Access and print the class-level property using the object
print(f"Brand: {c.brand}")


# Access and print the properties of the object
print(f"Model: {c.model}")
print(f"Year: {c.year}")


# Output:
# Brand: Toyoto
# Model: Corolla
# Year: 2022