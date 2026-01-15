# Indicates the beginning of the program.
print("PROGRAM STARTING...")


# It contains different error-prone operations like division by zero, invalid index access, 
# and key lookup in a dictionary.
try :
    # This will raise FileNotFoundError
    f = open("Demo.txt", "r")
    f.read()

except FileNotFoundError as e :
    print(e)
finally :
    print("Finally Block Executed.")

# Indicating the end of the program
print("PROGRAM ENDED...")


# Output:
# PROGRAM STARTING...
# [Errno 2] No such file or directory: 'Demo.txt'
# Finally Block Executed.
# PROGRAM ENDED...