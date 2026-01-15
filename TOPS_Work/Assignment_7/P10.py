# 10.	Write a Python program to sort a list using both sort() and sorted().

# sort() → Modifies the list in place.
# 1. Define the list
mylist = ["orange", "mango", "kiwi", "pineapple", "banana"]

# Sort using sort() (modifies the list in place)
mylist.sort()
print(mylist)           # Output: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']


# 2. Define the list
mylist = ["orange", "mango", "kiwi", "pineapple", "banana"]

# Sort in descending order using sort()
mylist.sort(reverse = True)
print(mylist)           # Output: ['pineapple', 'orange', 'mango', 'kiwi', 'banana']




# sorted() → Returns a new sorted list without changing the original list.
# 3. Define the list
mylist = [100, 50, 77, 97, 45, 23]

# Use sorted() to sort without modifying the original list
i = sorted(mylist)
print(i)            # Output: [23, 45, 50, 77, 97, 100]

# 4. Define the list
mylist = [100, 50, 77, 97, 45, 23]

# Use sorted() in descending order
i = sorted(mylist, reverse = True)
print(i)            # Output: [100, 97, 77, 50, 45, 23]



# 5. Print original list to show it remains unchanged
print(mylist)       # Output: [100, 50, 77, 97, 45, 23]