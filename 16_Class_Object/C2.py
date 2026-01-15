# Task 5: Make a class Person with attributes name and age.
# Write a method greet() that prints:
# Hello, my name is <name> and I am <age> years old.


class Person:
    name = 'Drashti'
    age = 21
    
    def __init__(self, name, age):    
        self.name = name
        self.age = age    

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

P1 = Person('Sejal', 29)
P1.greet()

# OP: Hello, my name is Sejal and I am 29 years old.