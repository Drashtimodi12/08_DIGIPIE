# Task 6: Create a class Employee with:
# class attribute: company = "Google"
# instance attributes: name, salary
# Create 3 objects and print all details.

class employee:
    company = 'Google'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
e1 = employee('drashti', 10000.00)
e2 = employee('sejal', 3000.00)
e3 = employee('atifa', 9000)


print(f'Name: {e1.name}, Salary: {e1.salary}')
print(f'Name: {e2.name}, Salary: {e2.salary}')
print(f'Name: {e3.name}, Salary: {e3.salary}')

# OP: 
# Name: drashti, Salary: 10000.0
# Name: sejal, Salary: 3000.0
# Name: atifa, Salary: 9000