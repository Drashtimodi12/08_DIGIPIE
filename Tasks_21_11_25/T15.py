# Create a class Rectangle that takes length and width as inputs. Add a method area() that returns 
# the area of the rectangle and another method perimeter() that returns its perimeter. 
# Create an object and display both values.

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return f"Area of rectangle: {self.length * self.width}."
    
    def perimeter(self):
        return f"Perimeter of rectangle: {2 * self.length + self.width}."
    
r1 = Rectangle(12, 6)
print(r1.area())
print(r1.perimeter())
# OP:
# Area of rectangle: 72.
# Perimeter of rectangle: 30.