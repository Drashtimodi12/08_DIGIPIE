# 5.	Write a Python program to open a file in write mode, write some text, and then close it. 

# Open the file in write mode
with open("P5.txt", "w") as file :
    # Write some text to the file
    file.write("Hello PYTHON\n")  # Write to file
    file.write("This is just sample file.\n")

# The file is automatically closed when the with block is exited
print("Text written to the file successfully.")
file.close()


# Output:
# (P5.txt)
# Hello PYTHON
# This is just sample file.

# Text written to the file successfully.