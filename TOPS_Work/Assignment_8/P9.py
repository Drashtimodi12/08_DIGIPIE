# 9.	Write a Python program to create a file and print the string into the file. 

# Open the file in write mode
with open("P9.txt", "w") as file :
    text = "This is simple string."
    print(text, file=file)  # Print the string directly into the file

print("String written successfully to P9.txt")

# Output:
# (P9.txt)
# This is simple string.

# String written successfully to P9.txt