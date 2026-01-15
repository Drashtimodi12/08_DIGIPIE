# 7.	Write a Python program to read the contents of a file and print them on the console.

# Open the file in read mode and print its contents
with open("P6.txt", "r") as file :
    content = file.read()       # Read the entire file content
    print("File Contents:\n", content)  # Print the file data

# Output:
# File Contents:
#  Python Priogram.
