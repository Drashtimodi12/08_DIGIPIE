# Indicates the beginning of the program.
print("PROGRAM STARTING...")


# It contains different error-prone operations like division by zero, invalid index access, 
# and key lookup in a dictionary.
try:
    l = [10, 20, 30]
    print(l[5])  # List index 5 does not exist, causing IndexError

except IndexError as e:
    print("Exception caught:", e)
finally:
    print("Finally block executed.")

print("Program ended.")

# Output:
# Program starting...
# Exception caught: list index out of range
# Finally block executed.
# Program ended.