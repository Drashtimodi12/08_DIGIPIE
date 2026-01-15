# 13.	Write a Python program to demonstrate handling multiple exceptions. 

try:
    # File handling (FileNotFoundError)
    file_name = "P9.txt"
    with open(file_name, "r") as file:
        content = file.read()
        print("File Content:", content)

    # Division (ZeroDivisionError)
    result = 10 / 0  # This will cause a ZeroDivisionError
    print(f"Result of Division: {result}")

    # Dictionary Key Access (KeyError)
    student = {"name": "Drashti", "age": 20}
    print("Student Marks:", student["marks"])  # KeyError

except FileNotFoundError:
    print("Error: The file you are trying to open does not exist.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter a valid number.")
except KeyError:
    print("Error: The key you are trying to access does not exist in the dictionary.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Program execution completed.")
