# remove():- Removing a Specific Item.
# If there are more than one item with the specified value, the remove() method removes the first occurrence
mylist = ["apple", "banana", "kiwi", "banana"]
mylist.remove("banana")
print(mylist)       # Output: ['apple', 'kiwi', 'banana']

# pop():- Removing an Item by Specified Index (pop() removes by index, last item if not specified)
mylist = ["apple", "banana", "kiwi", "banana"]
mylist.pop(1)        # Removes 'banana' at index 1
print(mylist)       # Output: ['apple', 'kiwi', 'banana']
mylist.pop()        # Removes last item
print(mylist)       # Output: ['apple', 'kiwi']

# del():- Removing an Item Using del (can also delete entire list)
mylist = ["apple", "banana", "kiwi", "banana"]
del mylist[0]       # Removes 'apple'
print(mylist)       # Output: ['banana', 'kiwi', 'banana']
del mylist          # Delete the entire list

# Clear():- Clearing a List (removes all elements but keeps the list)
# Clear the list content:
mylist = ["apple", "banana", "kiwi", "banana"]
mylist.clear()          # Clear the list content:
print(mylist)           # Output: []