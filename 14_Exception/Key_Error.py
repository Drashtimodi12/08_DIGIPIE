# Indicates the beginning of the program.
print("PROGRAM STARTING...")


# It contains different error-prone operations like division by zero, invalid index access, 
# and key lookup in a dictionary.
try :
    d = {"python" : "1", "java" : "2"}
    print(d["C"])   # "C" key does not exist in the dictionary, causing KeyError


except KeyError as e :
    print(e)
finally :
    print("Finally Block Executed.")

# Indicating the end of the program
print("PROGRAM ENDED...")


# Output:
# PROGRAM STARTING...
# 'C'
# Finally Block Executed.
# PROGRAM ENDED...