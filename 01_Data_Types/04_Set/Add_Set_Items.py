# Add Items:- Once a set is created, you cannot change its items, but you can add new items.

# add():- To add one item to a set use the add() method.
# If you try to add an existing item, it won’t be added (since sets do not allow duplicates).
myset = {"apple", "banana", "cherry"}
myset.add("orange")
myset.add("apple")
print(myset)        # Output: {'orange', 'apple', 'banana', 'cherry'}

# update():- To add items from another set into the current set, use the update() method.
s1 = {"apple", "banana", "cherry"}
s2 = {"orange", "pineapple"}
s1.update(s2)
print(s1)       # Output: {'banana', 'pineapple', 'cherry', 'apple', 'orange'}

# Add Any Iterable:- The object in the update() method does not have to be a set, it can be any iterable object 
# (tuples, lists, dictionaries etc.).
myset = {"apple", "banana", "cherry"}
mylist = ["orange", "pineapple"]
myset.update(mylist)
print(myset)        # Output: {'banana', 'orange', 'apple', 'cherry', 'pineapple'}


# Adding Key Names from Dictionary (update()):- When using update() with a dictionary, only the keys will be added.
myset = {"apple", "banana"}
mydict = {"grape": 5, "kiwi": 8}
myset.update(mydict)  # Only keys are added
print(myset)        # Output: {'apple', 'banana', 'kiwi', 'grape'}