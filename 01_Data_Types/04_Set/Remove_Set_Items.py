# Removing a Specific Item (remove()):- The remove() method removes a specified item from the set. 
# If the item does not exist, it raises an error.
myset = {"java", "php", "html"}
myset.remove("php")
print(myset)        # Output: {'java', 'html'}

# # If the item to remove does not exist, remove() will raise an error.
# myset = {"java", "php", "html"}
# myset.remove("python")
# print(myset)        # This will raise an error!



# Removing an Item Safely (discard()):- The discard() method removes an item but does not raise an error if the item is missing.
myset = {"java", "php", "html"}
myset.discard("python")
print(myset)        # Output: {'html', 'php', 'java'}

# Removing a Random Item (pop()):- The pop() method removes a random item from the set.
# Since sets are unordered, you don’t know which item will be removed.
myset = {"java", "php", "html"}
i = myset.pop()
print(i)            #removed item               # Output: html
print(myset)        #the set after removal      # Output: {'java', 'php'}

# Removing All Items (clear()):- The clear() method removes all elements from the set, making it an empty set.
myset = {"java", "php", "html"}
myset.clear()
print(myset)        # Output: set()

# Deleting the Set (del):- The del keyword completely deletes the set.
# Trying to access the set after deletion will raise an error.
myset = {"java", "php", "html"}
del myset
print(myset)          #this will raise an error because the set no longer exists
