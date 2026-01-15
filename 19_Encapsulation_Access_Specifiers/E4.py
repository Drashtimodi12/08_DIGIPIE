# Student Marks Encapsulation
# Requirements
# Class Student
# Private:
# __name
# __marks
# Set marks (0–100 only)
# Get marks
# Create a method grade():
# A (>=90), B (>=75), C (>=50), Fail


class Student:

    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_name(self):
        return self.__name
    
    def get_mark(self):
        return self.__marks
    
    def set_mark(self):
        marks = float(input("Enter total Marks: "))
        if 0 <= marks <= 100:
            self.__marks = marks
            print(f"Your marks is: {marks}")
        else:
            print("Invalid marks! Marks must be greater than 0 and less than eqaul to 100.")

    def grade(self):
        if self.__marks >= 90:
            print("Grade A.")
        elif self.__marks >= 75:
            print("Drade B.")
        elif self.__marks >= 50:
            print("Grade C.")
        else:
            print("Grade E. You are fail.")

s1 = Student("Drashti", 76)
print(f"Name: {s1.get_name()}")
s1.set_mark()
s1.grade()
# OP:
# Name: Drashti
# Enter total Marks: 76
# Your marks is: 76.0
# Drade B.