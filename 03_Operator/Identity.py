# Identity Operators: is, is not

# Compare two lists using == and is, explain result.
a = [1, 2, 3]
b = [1, 2, 3]
print("Using == :", a == b)
print("Using is operator: ", a is b)
# OP
# x == y : True
# x is y : True

print("\n===========================\n")



# Check if two variables point to same memory location.
x = [10, 20, 30]
y = x   

print("x == y :", x == y)     
print("x is y :", x is y)    
# OP:
# Using == : True
# Using is operator:  False  


print("\n===========================\n")


# Using `is not` operator
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)       # False (Different lists, different memory locations)
print(x is not y)   # True (Since they are different objects)
print(z is x)       # True 

print("\n===========================\n")

# Checking with None
z = None
print(z is None)   # True (None is a special object in Python)