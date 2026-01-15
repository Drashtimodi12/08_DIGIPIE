# Copy a List:- You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, 
# and changes made in list1 will automatically also be made in list2.

# copy():- You can use the built-in List method copy() to copy a list.
mylist = ["apple", "banana", "cherry"]
newlist = mylist.copy()
print(newlist)       # Output: ['apple', 'banana', 'cherry']

# list():- Another way to make a copy is to use the built-in method list().
mylist = ["apple", "banana", "cherry"]
newlist = list(mylist)
print(newlist)       # Output: ['apple', 'banana', 'cherry']

# slice Operator:- You can also make a copy of a list by using the : (slice) operator.
mylist = ["apple", "banana", "cherry"]
newlist = mylist[:]
print(newlist)       # Output: ['apple', 'banana', 'cherry']