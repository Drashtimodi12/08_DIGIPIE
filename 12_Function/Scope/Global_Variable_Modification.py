# Global → accessible everywhere

# 10. Function with Global
x = 12
def myfun9():
    global x
    print("Value of x inside function:", x)
    x = 15
print(myfun9())  
print("Value of x outside function:", x)
# OP: Value of x inside function: 12
#     Value of x outside function: 15

print("\n===========================\n")

# Create a global variable count = 0, and a function that increases it by 1 each time it’s called.

count = 0 
def inc():
    global count
    count += 1
    print(f"number is: {count}")
inc()
inc()
# OP:
# number is: 1
# number is: 2

print("\n===========================\n")





# global Keyword → Needed if you want to modify a global variable inside a function.
a = 20      # Global Variable

def test() :
    global a       # Accessing the global variable
    a = 50         # Modifying global variable
    a += 20
    print(a)        # Output: 70 (modifies global a)

print("Before: ", a)        # Output: before: 20
test()                      # Output: 70
print("After: ", a)         # Output: after: 70
   