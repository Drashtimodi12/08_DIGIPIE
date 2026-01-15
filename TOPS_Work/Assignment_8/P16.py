# 16.	Write a Python program to handle file exceptions and use the finally block for closing the file. 

try :
    # Trying to open a non-existent file
    file = open("P9.txt", "r")

    # Read file content
    content = file.read()
    print("File Content Is: \n", content)
    
except FileNotFoundError as f :
    print(f)
except PermissionError as p: 
    print(p)
except Exception as e :
    print(e)


finally :
    try :
        file.close()        # Ensuring the file is closed
        print("\nFile closed successfully.")
    except NameError as n:
        print("\n", n)

# Output:
# File Content Is:
#  This is simple string.
# This is python Practical in this folder.

# File closed successfully.