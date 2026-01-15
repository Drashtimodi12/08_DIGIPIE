# Tuple:- Tuples are used to store multiple items in a single variable.
# A tuple is a collection of ordered and unchangeable items, allowing duplicate values.
# Tuples are written with round brackets().

# Create a Tuple and print:
mytuple = ("apple", "banana", "cherry")
print("Original Tuple:", mytuple)      # Output: Original Tuple: ('apple', 'banana', 'cherry')

# Ordered:- When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Unchangeable:- Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Allow Duplicates:- Since tuples are indexed, they can have items with the same value
mytuple = ("apple", "banana", "cherry", "kiwi", "mango")
print(mytuple)      # Output: ('apple', 'banana', 'cherry', 'kiwi', 'mango')

# Tuple Length:- To determine how many items a tuple has, use the len() function
mytuple = ("apple", "banana", "cherry", "kiwi", "mango")
print(len(mytuple))      # Output: 5

# Creating a tuple with one item (comma is required)
# # type():- From Python's perspective, tuples are defined as objects with the data type 'tuple'
mytuple = ("apple",)
print("Tuple with one element:", mytuple)       # Output: Tuple with one element: ('apple',)
print(type(mytuple))      # Output: <class 'tuple'>

# Without a comma, it's just a string
a = ("apple")         #This is not tuple
print("List with one element:", a)         # Output: List with one element: apple
print(type(a))      # Output: <class 'str'>

# Tuples can contain different data types
t1 = ("apple", "banana", "cherry")
t2 = (1, 6, 8, 45, 0)
t3 = (True, False, True)
# A tuple can contain different data types:
t4 = ("apple", 32, True, 45, "orange")
print(t1)       # Output: ('apple', 'banana', 'cherry')
print(t2)       # Output: (1, 6, 8, 45, 0)
print(t3)       # Output: (True, False, True)
print(t4)       # Output: ('apple', 32, True, 45, 'orange')

# tuple() Constructor:- It is also possible to use the tuple() constructor to make a tuple.
mytuple = tuple(("apple", "banana", "cherry", "kiwi", "mango"))
print("Tuple Constructor: ", mytuple)       # Output: Tuple Constructor:  ('apple', 'banana', 'cherry', 'kiwi', 'mango')