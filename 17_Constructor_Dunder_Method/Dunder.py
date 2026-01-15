# Define a class named Point
class Point:
    def __init__(self, x, y):
        # Constructor (__init__ method)
        # Initializes a Point object with x and y coordinates.
        self.x = x
        self.y = y

    def __str__(self):
        # __str__:- Returns a user-friendly string representation of the Point object.
        # This is used when printing the object using print().
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        # __repr__:- Returns an official string representation of the Point object.
        # Used when calling repr() function or in interactive console.
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        # __add__:- Overloads the '+' operator to add two Point objects.
        # It returns a new Point with summed x and y coordinates.
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented  # If the object is not of type Point

    def __eq__(self, other):
        # __eq__:- Overloads the '==' operator to compare two Point objects.
        # Returns True if both x and y coordinates are equal.
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented  # If the object is not of type Point

# Create two Point instances
point1 = Point(2, 3)
point2 = Point(4, 5)

# Use __str__ method (calls str(point1))
print(point1)  # Output: Point(2, 3)

# Use __repr__ method (calls repr(point1))
print(repr(point1))  # Output: Point(2, 3)

# Use __add__ method (calls point1 + point2)
point3 = point1 + point2
print(point3)  # Output: Point(6, 8)

# Use __eq__ method (calls point1 == point2)
print(point1 == point2)  # Output: False (since (2,3) != (4,5))
print(point1 == Point(2, 3))  # Output: True (since (2,3) == (2,3))