# Polymorphism With Function
# Requirements
# Create a function show_details(obj) that calls details() method.
# Create two classes: Student and Teacher
# Both must have details() method (different outputs).
# Pass objects of both to the function.

class Student:
    def details(self):
        print("Student have ID number and Name...")

class Teacher:
    def details(self):
        print("Teacher have figerprint to clock in and out...")


def show_details(obj):
    obj.details()

t = Teacher()
show_details(t)

s = Student()
show_details(s)
# OP:
# Teacher have figerprint to clock in and out...
# Student have ID number and Name...