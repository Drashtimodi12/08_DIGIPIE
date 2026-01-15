# 8.	How to check the type of a variable dynamically using type().

# You can use __name__ to get the type name as a string.

name = "Drashti"
print(type(name).__name__)  # Output: <class 'str'>

age = 22
print(type(age).__name__)  # Output: <class 'int'>

height = 5.4
print(type(height))  # Output: <class 'float'>

is_student = True
print(type(is_student))  # Output: <class 'bool'>