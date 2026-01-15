# Shape Area
# Requirements:
# Abstract class Shape:
# Abstract method: area()
# Child classes: Circle and Rectangle
# Implement area() in each class.
# Create objects and print areas.


from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, redius):
        self.redius = redius
    def area(self):
        print("Area of Circle= ", 3.14 * self.redius * self.redius)
        

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print("Area of Rectangle= ", self.length * self.width)

c = Circle(5)
c.area()
# OP: Area of Circle=  78.5


r = Rectangle(10, 15)
r.area()
# OP: Area of Rectangle=  150