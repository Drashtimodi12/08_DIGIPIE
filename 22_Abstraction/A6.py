# Student Marks System
# Requirements:
# Abstract class Student:
# Abstract method: grade()
# Child class: ScienceStudent → implement grade() based on marks
# Concrete method in parent: display_name(name)
# Create object and test methods.

from abc import ABC, abstractmethod

class Student(ABC):

    @abstractmethod
    def grade(self):
        pass

    def display_name(self, name):
        print(f"Your name is {name}")

class ScienceStu(Student):
    def grade(self):
        stu_mark = float(input("Enter Marks to check grade: "))
    
        if stu_mark >= 90:
            print("Grade A.")
        elif stu_mark >= 75:
            print("Grade B.")
        elif stu_mark >= 60:
            print("Grade C.")
        elif stu_mark >= 50:
            print("Grade D.")
        else:
            print("Fail")
        
s = ScienceStu()
s.display_name('Drashti')
s.grade()
# OP:
# Your name is Drashti
# Enter Marks to check grade: 67
# Grade C.