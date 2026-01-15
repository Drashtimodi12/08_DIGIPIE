# Create a class Car with attributes brand and color. Create one object and then change its color 
# after creation.

class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

c1 = Car('Tesla', 'Black')
c1.color = 'Black'

print(f"{c1.brand} is most commanly sold {c1.color} color car.")
# OP:
# Tesla is most commanly sold Black color car.