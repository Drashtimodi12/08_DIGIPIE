# Create a class Student with name and grade (default value "A") attributes. If grade is not given, use the default value.


class Student:

    def __init__(self, name, grade = 'A'):
        self.name = name
        self.grade = grade

s1 = Student('Drashti')
s1.grade = 'B'
print(f"I am {s1.name} and grade is {s1.grade}.")

s2 = Student('Sejal')
print(f"I am {s2.name} and grade is {s2.grade}.")
# OP:
# I am Drashti and grade is B.
# I am Sejal and grade is A.