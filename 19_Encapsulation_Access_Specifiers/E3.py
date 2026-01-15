# Employee Salary Encapsulation
# Requirements
# Create a class Employee
# Private attributes:
# __name
# __salary
# Add setter with validation:
# Salary must be > 0
# Add getter methods
# Create object and print valid/invalid salary cases.

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name
    
    def get_salary(self):
        return self.__salary
    
    def set_name(self):
        new_name = input("Enter name: ")
        self.__name = new_name

    def set_salary(self):
        new_salary = float(input("Enter New salary: "))
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Salary must be greater than 0.")

e1 = Employee('Drashti', 10000)

print("Name:", e1.get_name())
print("Salary:", e1.get_salary())

print("\nTrying invalid salary:")
e1.set_name()

print("\nTrying valid salary:")
e1.set_salary()      

print("\nUpdated Details:")
print("Name:", e1.get_name())
print("Salary:", e1.get_salary())
# OP:
# Name: Drashti
# Salary: 10000

# Trying invalid salary:
# Enter name: Daizy

# Trying valid salary:
# Enter New salary: 10000

# Updated Details:
# Name: Daizy
# Salary: 10000.0