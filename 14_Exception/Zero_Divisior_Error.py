# Exception handling in Python is a mechanism that allows us to detect and handle runtime errors (exceptions) gracefully, 
# preventing program crashes. The try-except block is used to catch and handle these exceptions.


# Indicates the beginning of the program.
print("PROGRAM STARTING...")


# It contains different error-prone operations like division by zero, invalid index access, 
# and key lookup in a dictionary.
try :
    a = 10
    b = a / 0       # This will raise ZeroDivisionError
    print(b)
except ZeroDivisionError as e :
    print(e)
finally :
    print("Finally Block Executed.")

# Indicating the end of the program
print("PROGRAM ENDED...")


# Output:
# PROGRAM STARTING...
# division by zero
# Finally Block Executed.
# PROGRAM ENDED...