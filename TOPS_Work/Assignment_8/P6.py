# 6.	Write a Python program to create a file and write a string into it. 

# Open a file in write mode and write a string into it
with open("P6.txt", "w") as file :
    file.write("Python Priogram.\n")        # Write data to the file

print("File created and data written successfully.")

# Output:
# (P6.txt)
# Python Priogram.

# File created and data written successfully.