"""What is Function in Python?
A function is a block of code which only runs when it is called. 
It also helps to reuse the code. It starts with the keyword 'def' followed by the function name and parentheses ().
You can pass data, known as parameters, into a function.

Types of Functions in Python:
1. Built-in Functions   -> print(), input(), len(), type(), range(), round(), etc.
2. User-defined Functions
3. Anonymous Functions (Lambda Functions) 
4. Recursive Functions
"""


# -----------In Built Functions-----------

print("hello".title())      # Hello

for i in range(1, 6):
    print(i)
    # 1
    # 2 
    # 3
    # 4
    # 5

a = round(32.4443, 2)
print(a)    # 32.44

x ="Tops technologies pvt ltd".split()
print(x)
# OP: ['Tops', 'technologies', 'pvt', 'ltd']











# Print with raw string (r prefix ignores escape sequences)
print(r"python is \" oops lang.")   
# The 'r' prefix treats backslashes (\) as literal characters.
# Output: python is \" oops lang.


# Taking string input
name = input("Enter name : ")   # User enters a name
print(name)  
# OP:
# Enter name : drashti
# drashti


# Taking integer input
a = int(input("Enter number 1: "))  # Convert user input to an integer
b = int(input("Enter number 2: "))  # Convert user input to an integer

print(a + b)  # Adds two numbers and prints the result
print(int(a) + int(b))  # Another way of addition (redundant type conversion)
# OP:
# Enter number 1: 3
# Enter number 2: 4
# 7
# 7


# Type conversion example
c = "100"  # String value
d = int(c)  # This line will work fine
print(type(d))  
# Output: <class 'int'>

# e = "100O"  # Invalid integer (contains letter 'O')
# f = int(e)  # This line will raise an error
# print(type(f))  
# Output: <class 'str'> (but will not execute due to error)

# id function example
A = 10
print(id(A))  
# Output: e.g: 140726123456000 (memory address of the variable A)

# String split example
name = "Tops technologies pvt ltd".split()      # Splitting the string into a list based on spaces
print(name)     
# Output: ['Tops', 'technologies', 'pvt', 'ltd']

name = "Tops technologies pvt ltd".split("o")   # Splitting the string where the letter 'o' appears
print(name)     
# Output: ['T', 'ps techn', 'l', 'gies pvt ltd']

# length of the string
name = "Tops technologies pvt ltd"
print(len(name))  
# Output: 25 (total number of characters including spaces)

# String formatting example
fname = "Farukh"
lname = "Shaikh"
# Using format method
print("my name is {1} and my surname is {0}".format(fname,lname))   # Output: my name is Shaikh and my surname is Farukh
# Using f-string
print(f"my name is {fname} and surname is {lname}")     # Output: my name is Farukh and surname is Shaikh







