# Lists in Python:       Lists are used to store multiple items in a single variable.
# A list is a collection that is ordered, changeable, and allows duplicate values.
# Lists are created using square brackets [].
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# Ordered:-      It means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# Changeable:-    The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Creating a list
mylist = ['apple', 'banana', 'grapes']
print(mylist)   # Output: ['apple', 'banana', 'grapes']

# List Allow Duplicate Values
mylist = ["apple", "banana", "cherry", "apple", "cherry"]
print(mylist)   # Output: ['apple', 'banana', 'cherry', 'apple', 'cherry']

# Checking the length of a list 
mylist = ['apple', 'banana', 'grapes']
print(len(mylist))      # Output: 3

# Lists can store different data types
list1 = ['apple', 'banana', 'grapes']
list2 = [1, 3, 6, 9]
list3 = [True, False, True]
print(list1, list2, list3)    # Output: ['apple', 'banana', 'grapes'] [1, 3, 6, 9] [True, False, True]
# Accessing list items using index
print(list1[0])     # Output: apple

list4 = ['apple', 3, True, 8, 'banana']
print(list4)       # Output: ['apple', 3, True, 8, 'banana']

# Checking the type() of a list
list4 = ['apple', 3, True, 8, 'banana']
print(type(list4))      # Output: <class 'list'>

# Creating a list using the list() constructor
mylist = list(("apple", "banana", "cherry")) # Double parentheses are required
print(mylist)       # Output: ['apple', 'banana', 'cherry']