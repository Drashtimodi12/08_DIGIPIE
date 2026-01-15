# EXCEPTION:
# iT is an event or an error that occurs during the execution of a program, disrupting the normal flow of instructions. 
# Exceptions can be caused by a variety of reasons such as invalid user input, file not found, division by zero, 
# etc. When an exception occurs, the program terminates abruptly unless the exception is handled properly.

# EXAMPLE:
a = 10
b = 0
result = a / b  # This will raise a ZeroDivisionError
print(result)


# EXCEPTION HANDLING:
# iT is a mechanism to handle runtime errors or exceptions in a controlled way. It allows a program to continue execution 
# (or terminate gracefully) despite the presence of errors. Exception handling involves using specific constructs 
# like try, catch, except, finally, etc., to catch exceptions and define responses to them.

# EXAMPLE:
print("PROGRAM STARTING...")    # Indicates the beginning of the program.

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

print("PROGRAM ENDED...")   # Indicating the end of the program

# OP:
# PROGRAM STARTING...
# division by zero
# Finally Block Executed.
# PROGRAM ENDED...