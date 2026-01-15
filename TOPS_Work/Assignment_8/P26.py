# 26.	Write a Python program to show hybrid inheritance. 

# Parent class
class School :
    def school_name(self) :
        print("SBV School.")

# Intermediate Parent class (Multiple Inheritance)
class Teacher(School) :
    def subject(self) :
        print("Maths Teacher.")

class Student(School) :
    def grade(self) :
        print("Students is in 10th grade.")

# Child class inheriting from both Teacher and Student
class Moniter(Teacher, Student) :
    def responsibility(self) :
        print("Moniter Maintains Discipline.")

# Creating an object of Monitor class
m = Moniter()
m.school_name()   # Inherited from School
m.subject()       # Inherited from Teacher
m.grade()         # Inherited from Student
m.responsibility()# Own method


# Output:
# SBV School.
# Maths Teacher.
# Students is in 10th grade.
# Moniter Maintains Discipline.