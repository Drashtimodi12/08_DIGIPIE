# 7.	Write a Python program to update a list using insert() and append(). 

# Define the list
mylist = ["apple", "banana", "kiwi"]

# Update an existing element (replace "banana" with "mango")
mylist.insert(1, "mango")
print(mylist)               # Outpu: ['apple', 'mango', 'banana', 'kiwi']

# Append "orange" to the end of the list
mylist.append("orange")
print(mylist)               # Output: ['apple', 'mango', 'banana', 'kiwi', 'orange']