# 12.	Write a Python program to insert elements into an empty list using a for loop and append().

# Define an empty list
mylist = [ ]

# List of elements to insert
element = [30, 21, 78, 56, 92, 60]

# Insert elements into the empty list using a for loop and append()
for i in element :
    mylist.append(i)
    # mylist.sort()           # Output: List:  [21, 30, 56, 60, 78, 92]

# Print the updated list
print("List: ", mylist)     # Output: List:  [30, 21, 78, 56, 92, 60]