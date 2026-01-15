# 6.	Write a Python program to remove elements from a list using pop() and remove().

# Define the list
mylist = ["apple", "banana", "kiwi", "mango", "orange"]

# Remove element at index 3 (which is "mango")
mylist.pop(3)
print(mylist)           # Output: ['apple', 'banana', 'kiwi', 'orange']

# Remove the element "apple" from the list
mylist.remove("apple")
print(mylist)           # Output: ['banana', 'kiwi', 'orange']