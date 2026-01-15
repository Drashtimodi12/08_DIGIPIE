# Indicates the beginning of the program.
print("PROGRAM STARTING...")


# It contains different error-prone operations like division by zero, invalid index access, 
# and key lookup in a dictionary.
try :
    x = 5
    x.append(10)        # This will raise AttributeError

except AttributeError as e :
    print(e)
finally :
    print("Finally Block Executed.")

# Indicating the end of the program
print("PROGRAM ENDED...")


# Output:
# PROGRAM STARTING...
# 'int' object has no attribute 'append'
# Finally Block Executed.
# PROGRAM ENDED...