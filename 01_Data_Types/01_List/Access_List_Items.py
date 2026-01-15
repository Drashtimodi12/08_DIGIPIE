# Accessing list items using index and index number
mylist = ['apple', 'banana', 'cherry']
print(mylist[1])    # Output: banana

# Accessing list items using negative indexing like: -2 refers to the second last item etc.
mylist = ['apple', 'banana', 'cherry', 'kiwi', 'grapes']
print(mylist[-1])   # Output: grapes
print(mylist[-4:-1])    # Output: ['banana', 'cherry', 'kiwi']

# Range of Indexes: Accessing a range of items (index 1 to 2)
# Remember that the first item has index 0.
mylist = ['apple', 'banana', 'cherry', 'kiwi', 'grapes']
print(mylist[1:3])  # Output: ['banana', 'cherry']

# Checking if an item exists in the list
mylist = ['apple', 'banana', 'cherry', 'kiwi', 'grapes']
if 'apple' in mylist:
    print('Yes, Apple is in the list.')  # Output: Yes, Apple is in the list.