"""# -----------User Defined Functions-----------
Definition:  It is a block of reusable code written by the user to perform a specific operation, 
    which can be called whenever needed.

Syntax:
    def function_name(parameters):
        Optional docstring to describe the function
            # statements
        return value   # optional

    
Defined by user using def keyword.
Can take parameters/arguments.
Can return a value using return.
Helps in code reuse, modularity, and readability.
"""

# 1. Function without argument and without return type
def myfun1():
    print("This is my first function.")
myfun1()
# Output: This is my first function.

print("\n-------------------------------------\n")



# 2. Function with one argument and without return type
def myfun2(name):
    print(f"Hello, {name}!")
myfun2("Drashti")
# Output: Hello, Drashti!
print("\n-------------------------------------\n")




# 3. Function with multiple arguments and without return type
def myfun3(a, b, c):
    sum = a + b + c
    print(f"The sum of {a}, {b}, {c} is {sum}.")
myfun3(5, 10, 1)
# Output: The sum of 5, 10, 1 is 16.
print("\n-------------------------------------\n")




# 4. Function with keyword arguments
def myfun4(name, age, city):
    print("Address Details: ", city)    
    print(f"My name is {name}. I am {age}. i am leave in {city}.")      
myfun4(age=25, name="Drashti", city="Ahmedabad")
# Output: Address Details: Ahmedabad
#         My name is Drashti. I am 25. i am leave in Ahmedabad.
print("\n-------------------------------------\n")




# 5. Function with default arguments
def myfun5(name='Drashti', age=25):
    print(f"My name is {name}. I am {age} years old.")
myfun5()
myfun5("Anjli", 24)
# Output: My name is Drashti. I am 25 years old.
#         My name is Anjli. I am 24 years old.
print("\n-------------------------------------\n")




# 6. Passing list in function
def myfun6(fruits):
    for i in fruits:
        print(i)
f = ['Mango', 'Apple', 'Banana']
myfun6(f)
# Output: Mango
#         Apple
#         Banana
print("\n-------------------------------------\n")




# 7. Function with return value
def myfun7(a):
    return 2 * a
result = myfun7(5)
print(f"The result is {result}.")  
# Output: The result is 10.



