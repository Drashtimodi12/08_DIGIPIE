# 11.	Write a Python program to check the current position of the file cursor using tell(). 

with open("P9.txt", "r") as file :
    print(f"Initial cursor position: {file.tell()}")  # Cursor at the start
    file.read(10)  # Read first 10 characters
    print(f"Cursor position after reading 10 characters: {file.tell()}")  # Check position
    file.read()  # Read the rest of the file
    print(f"Cursor position after reading the entire file: {file.tell()}")  # End position

# Output:
# Initial cursor position: 0
# Cursor position after reading 10 characters: 10  
# Cursor position after reading the entire file: 64