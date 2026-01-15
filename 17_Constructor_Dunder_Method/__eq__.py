# __eq__(self, other): This dunder method allows custom behavior for == operator.
# When you write obj1 == obj2, Python internally calls obj1.__eq__(obj2).

class Student:
    # Constructor to store marks
    def __init__(self, marks):
        self.marks = marks

    # Custom == comparison
    # It returns True if marks of both student objects are equal.
    def __eq__(self, other):
        return self.marks == other.marks

# Creating two student objects with same marks
s1 = Student(90)
s2 = Student(90)

# s1 == s2 calls s1.__eq__(s2)
print(s1 == s2)
# OP: True