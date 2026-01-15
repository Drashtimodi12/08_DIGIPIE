# 30.	Write a Python program to demonstrate string slicing.

# Define a string
a = 'Hello World!'

# 1. Accessing the first 5 characters (from index 0 to 4)
print("First 5 characters:", a[:5])

# 2. Accessing characters from index 7 to the end
print("From index 7 onwards:", a[7:])

# 3. Accessing characters from index 2 to 8 (not including 8)
print("Slice from index 2 to 8:", a[2:8])

# 4. Accessing every second character starting from index 0
print("Every second character:", a[::2])

# 5. Accessing the string in reverse (using negative step)
print("Reversed string:", a[::-1])