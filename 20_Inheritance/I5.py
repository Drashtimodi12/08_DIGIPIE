# Hybrid Inheritance – Person → Student & Worker → Intern
# Requirements:
# Class Person
# method: details()
# Class Student(Person)
# method: study()
# Class Worker(Person)
# method: work()
# Class Intern(Student, Worker)
# method: intern_info()
# Create object of Intern and call all methods available.

class Person:
    def details(self):
        name = input("\nEnter person name: ")
        print(f"Your name is {name}")

class Student(Person):
    def study(self):
        print("I am studying as a student.")

class Worker:
    def work(self):
        print("I am doing worker-related tasks.")

class Intern(Student, Worker):
    def intern_info(self):
        print("\nI am an intern, so I study and work both.")

s = Student()
s.details()
s.study()



i = Intern()
i.details()
i.intern_info()
i.study()
i.work()
# OP:
# Enter person name: drashti
# Your name is drashti
# I am studying as a student.

# Enter person name: daizy
# Your name is daizy

# I am an intern, so I study and work both.
# I am studying as a student.
# I am doing worker-related tasks.