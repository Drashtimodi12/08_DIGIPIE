# 29.	Write a Python program to show method overloading. 

class Calculator :
    def add(self, a, b = 0, c = 0) :
        return a + b + c 

# Create an instance of Calculator
calc = Calculator()

# Call the add method with different numbers of arguments
print(calc.add(10))       # Output: 10
print(calc.add(10, 20))   # Output: 30
print(calc.add(10, 20, 30))  # Output: 60