# Set:- Sets are used to store multiple items in a single variable. Sets are written with curly brackets.
# A set is a collection which is unordered, unchangeable, and do not allow duplicate values..
# Set items are unchangeable, but you can remove items and add new items.

# Creating a Set:- You can create a set using {} or the set() constructor.
myset = {"apple", "banana", "mango"}
print(myset)        # Output: {'banana', 'mango', 'apple'}

# The set() Constructor:- It is also possible to use the set() constructor to make a set.
myset = set(("apple", "mango", "cherry"))   # note the double round-brackets
print(myset)        # Output: {'mango', 'apple', 'cherry'}



# Unordered:-   It means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable:-    Set items are unchangeable, meaning that we cannot change the items after the set has been created.

# Duplicates Not Allowed:- Sets cannot have two items with the same value. 
# The values (True and 1) and (False and 0) are considered the same value in sets, and are treated as duplicates:

myset = {"apple", "banana", "mango", "apple", "orange", "cherry", True, 1, 2}
print(myset)        # Output: {True, 2, 'mango', 'orange', 'banana', 'apple', 'cherry'}


# Get the Length of a Set:- To determine how many items a set has, use the len() function.
myset = {"apple", "banana", "mango", "orange", "cherry", True, 0}
print(len(myset))       # Output: 7

# Set Items - Data Types:- Set items can be of any data type:
s1 = {"apple", "banana", "cherry"}
print(s1)       # Output: {'cherry', 'banana', 'apple'}

s2 = {1, 5, 7, 9, 3}
print(s2)       # Output: {1, 3, 5, 7, 9}

s3 = {True, False, False}
print(s3)       # Output: {False, True}

s4 = {"mango", 34, True, 40, "orange"}
print(s4)       # Output: {True, 34, 'orange', 40, 'mango'}

# type():- From Python's perspective, sets are defined as objects with the data type 'set':
myset = {"mango", 34, True, 40, "orange"}
print(type(myset))       # Output: <class 'set'>

