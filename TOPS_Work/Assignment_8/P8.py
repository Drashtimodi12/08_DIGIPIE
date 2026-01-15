# 8.	Write a Python program to write multiple strings into a file. 

# Open the file in write mode
with open("P8.txt", "w") as file :
    file.write("Hello, this is a Python program.\n")
    file.write("We are writing multiple lines into a file.\n")
    file.write("File handling in Python is easy!\n")

print("Data written successfully to P7.txt")

# Output:
# (P8.txt)
# Hello, this is a Python program.
# We are writing multiple lines into a file.
# File handling in Python is easy!

# Data written successfully to P7.txt