# Hierarchical Inheritance – Shape → Circle & Square
# Requirements:
# Class Shape
# method: describe()
# Class Circle(Shape)
# method: area(radius)
# Class Square(Shape)
# method: area(side)
# Create objects of both and call methods.



class Shape:
    def describe(self):
        print("\nThis is a geometric shape.")

class Circle(Shape):
    def area(self):
        self.redius = float(input("\nEnter redius of circle: "))
        area_circle = 3.14 * self.redius * self.redius
        print("Circle Reduced is: ", area_circle)

class Square(Shape):
    def area(self):
        self.side = float(input("\nEnter side of square: "))
        area_square = self.side ** 2
        print("Square area is: ", area_square)

c = Circle()
c.describe()
c.area()

s = Square()
s.describe()
s.area()
# OP:
# This is a geometric shape.

# Enter redius of circle: 4
# Circle Reduced is:  50.24

# This is a geometric shape.

# Enter side of square: 9
# Square area is:  81.0