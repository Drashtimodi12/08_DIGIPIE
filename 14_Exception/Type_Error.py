# Indicates the beginning of the program.
print("PROGRAM STARTING...")


# It contains different error-prone operations like division by zero, invalid index access, 
# and key lookup in a dictionary.
try :
    a = 10 - "5"    # This will raise TypeError
    print(a)


except TypeError as e :
    print(e)
finally :
    print("Finally Block Executed.")

# Indicating the end of the program
print("PROGRAM ENDED...")


# Output:
# PROGRAM STARTING...
# unsupported operand type(s) for -: 'int' and 'str'
# Finally Block Executed.
# PROGRAM ENDED...