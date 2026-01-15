# Task 8: Create a class Rectangle with:
# instance attributes: length, width
# method area() that returns area
# Create 2 rectangles and print their areas.

class Rectangle:

    def __init__(self, len, wid):
        self.length = len
        self.width = wid

    def area(self):
        return self.width * self.length 
        
R1 = Rectangle(15, 10)

R1.area()
print(f"Rectangle Length= {R1.length}, \nWidth={R1.width} \nArea of Rectangle = {R1.area()}")
# OP:
# Rectangle Length= 15, 
# Width=10
# Area of Rectangle = 150