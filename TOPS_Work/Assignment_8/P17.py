# 17.	Write a Python program to print custom exceptions. 

# Define a custom exception class
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be between 18 and 60"):
        self.message = message

# Function to check age validity
def check_age(age):
    if age < 18 or age > 60:
        raise InvalidAgeError(f"Invalid Age: {age} is not allowed!")
    else:
        print(f"Valid Age: {age}")

# Main program
try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print("Custom Exception Caught:", e)
except ValueError:
    print("Error: Please enter a valid number.")
