# 20.	Write a Python program to demonstrate the use of local and global variables in a class. 

a = 20      # Global Variable

def test() :
    # global a       # Uncomment this line to modify the global variable
    a = 50
    a += 20
    print(a)        # Output: 70 (local scope)

print("******* GLOBAL ********")
print("Before: ", a)        # Output: before: 20 (global scope)
test()
print("After: ", a)         # Output: after: 20 (global scope)


# global Keyword → Needed if you want to modify a global variable inside a function.

a = 20      # Global Variable

def test() :
    global a       # Accessing the global variable
    a = 50         # Modifying global variable
    a += 20
    print(a)        # Output: 70 (modifies global a)

print("******* LOCAL ********")
print("Before: ", a)        # Output: before: 20
test()
print("After: ", a)         # Output: after: 70