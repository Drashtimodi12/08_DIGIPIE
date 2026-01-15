# Student Class using Encapsulation

class Student:

    # Constructor with private attributes
    def __init__(self, stu_name, stu_age, stu_marks):
        self.__name = stu_name      # private attribute
        self.__age = stu_age        # private attribute
        self.__marks = stu_marks    # private attribute

    # ---------------- GETTER METHODS ----------------
    def get_name(self):
        """Return student's name"""
        return self.__name
    
    def get_age(self):
        """Return student's age"""
        return self.__age

    def get_marks(self):
        """Return student's marks"""
        return self.__marks

    # ---------------- SETTER METHODS ----------------
    def set_name(self, new_stu_name):
        """Update student's name"""
        self.__name = new_stu_name

    def set_age(self, new_stu_age):
        """
        Update age with validation.
        Age must be between 5 and 100.
        """
        if 5 <= new_stu_age <= 100:
            self.__age = new_stu_age
        else:
            print("Invalid age! Age must be between 5 and 100.")

    def set_marks(self, new_stu_marks):
        """
        Update marks with validation.
        Marks must be between 0 and 100.
        """
        if 0 <= new_stu_marks <= 100:
            self.__marks = new_stu_marks
        else:
            print("Invalid marks! Marks must be between 0 and 100.")

# ---------------- TESTING THE CLASS ----------------

s1 = Student("Drashti", 21, 80)

print("----- Student Details -----")
print("Name:", s1.get_name())
print("Age:", s1.get_age())
print("Marks:", s1.get_marks())

# Testing Setters
s1.set_age(25)
s1.set_marks(90)

print("\n----- After Updating -----")
print("Updated Age:", s1.get_age())
print("Updated Marks:", s1.get_marks())
# OP:
# ----- Student Details -----
# Name: Drashti
# Age: 21
# Marks: 80

# ----- After Updating -----
# Updated Age: 25
# Updated Marks: 90