# Create a class called Person with attributes name and age. Create one object and print the person’s name and age.

class  Person:

    def __init__(self, name, age):
        self.n = name
        self.a = age


P1 = Person('Drashti', 21)
print(f"Person name is {P1.n} and I am {P1.a} years old.")



a = 10
b = a
print(b)
a = 30
print(a)
# OP:
# 10
# 30