# Employee Abstraction
# Requirements:
# Abstract class Employee:
# Abstract method: calculate_salary()
# Concrete method: display_name(name)
# Child classes: Developer and Designer
# Implement calculate_salary() differently in each child class.
# Create objects and test all methods.

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_name(self):
        self.emp_name = input("\nEnter your name: ")
        print(f"Employee Name: {self.emp_name}")


class Developer(Employee):
    def calculate_salary(self):
        base_salary = 3000
        diwali_bonus = float(input("Enter your Diwali Bonus: "))
        total = base_salary + diwali_bonus
        print(f"Developer Total Salary: {total}")


class Designer(Employee):
    def calculate_salary(self):
        base_salary = 5000
        diwali_bonus = float(input("Enter your Diwali Bonus: "))
        total = base_salary + diwali_bonus
        print(f"Designer Total Salary: {total}")


Dev = Developer()
Dev.display_name()
Dev.calculate_salary()
# OP:
# Enter your name: Drashti
# Employee Name: Drashti
# Enter your Diwali Bonus: 5000
# Developer Total Salary: 8000.0





Des = Designer()
Des.display_name()
Des.calculate_salary()
# OP:
# Enter your name: Daizy
# Employee Name: Daizy
# Enter your Diwali Bonus: 400
# Designer Total Salary: 5400.0