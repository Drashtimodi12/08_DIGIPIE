# Membership Operators:   in, not in


# Membership Operator: in, Not in
# used to check if a value exists in a sequence (like strings, lists, tuples) or keys in a dictionary.

# 1. Using `in` with a string
text = "Hello Python"
print("Python" in text)  # True (Substring "Python" is found in the string)
print("Java" in text)    # False ("Java" is not in the string)

# 2. Using `not in` with a string
print("Java" not in text)  # True (Because "Java" is not present in text)

# 3. Using `in` with a dictionary (checks for keys, not values)
student = {"name": "Alice", "age": 20, "city": "New York"}
print("name" in student)  # True (Key "name" exists in dictionary)
print("Alice" in student)  # False (Checks only keys, not values)

# 4. Using `not in` with a dictionary
print("gender" not in student)  # True (Key "gender" is not present)

print("\n===========================\n")




# Check if "a" is present in "Drashti".
a = 'Drashti'
print('a' in a)
# OP: True

print("\n===========================\n")




# Check if 10 is not in a list [5, 7, 8].
b = [5, 7, 8]
print(10 not in b)
# OP: True