# List Comprehension:- it offers a shorter syntax when you want to create a new list based on the values of an existing list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# Create a list with fruits containing the letter 'a'
newlist = []
for x in fruits :
    if "a" in x :
        newlist.append(x)
print(newlist)          #Output: ['apple', 'banana', 'mango']

# With list comprehension you can do all that with only one line of code
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# Create a list with fruits containing the letter 'e'
newlist = [x for x in fruits if "e" in x]
print(newlist)          #Output: ['apple', 'cherry']

# Condition:- it is like a filter that only accepts the items that evaluate to True.
# Syntax:- newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# Filter out 'apple' from the list
newlist = [x for x in fruits if x != "apple"]
print(newlist)          #Output: ['banana', 'cherry', 'kiwi', 'mango']

# Copy the entire list using list comprehension 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)          #Output: ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# Iterable:- The iterable can be any iterable object, like a list, tuple, set etc.
# You can use the range() function to create an iterable / Using range() to create a list of numbers
newlist = [x for x in range(10)]
print(newlist)          #Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using range() with a condition
newlist = [x for x in range(10) if x < 5]
print(newlist)          #Output: [0, 1, 2, 3, 4]


# Expression:- It is the current item in the iteration, but it is also the outcome, which you can manipulate before
# it ends up like a list item in the new list

# Convert all fruit names to uppercase
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)          #Output: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

# You can set the outcome to whatever you like:
# Replace all values with 'hello'
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)          #Output: ['hello', 'hello', 'hello', 'hello', 'hello']

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
# Replace 'banana' with 'orange', keep others unchanged
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != 'banana' else 'orange' for x in fruits]
print(newlist)          #Output: ['apple', 'orange', 'cherry', 'kiwi', 'mango']

# start name with a
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
for i in fruits:
    if i.startswith('a'):
        print(i)        
# OP: apple
    