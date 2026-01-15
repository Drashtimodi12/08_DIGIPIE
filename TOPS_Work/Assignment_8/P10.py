# 10.	Write a Python program to read a file and print the data on the console. 

# Open the file in read mode
with open("P8.txt", "r") as file :
    content = file.read()       # Read the entire file content

# Print the content on the console
print("File Contents:\n", content)  

# Output:
# (P8.txt)
# File Contents:
#  Hello, this is a Python program.
# We are writing multiple lines into a file.
# File handling in Python is easy!