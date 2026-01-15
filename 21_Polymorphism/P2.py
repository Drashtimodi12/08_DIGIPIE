# Shape Area (Common Method Name)
# Requirements
# Create class Circle with method area().
# Create class Square with method area().
# Create objects of both classes and call area() to show polymorphism.

class Circle:
    def area(self):
        r = 5
        print("Circle of area formula = 3.14*r*r.")

class Square:
    def area(self):
        s = 2
        print("Square of area formula = s * s.")

obj = Circle(), Square()

for i in obj:
    i.area()
# OP:
# Circle of area formula = 3.14*r*r.
# Square of area formula = s * s.