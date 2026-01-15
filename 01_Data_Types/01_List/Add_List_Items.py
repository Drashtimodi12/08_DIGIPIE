# Append Items:-  To add an item to the end of the list, use the append() method
mylist = ["apple", "banana", "charry"]
mylist.append("orange")
print(mylist)       # Output: ['apple', 'banana', 'charry', 'orange']

# Insert Items:-  To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# Insert() an item at a specific index
mylists = ["apple", "banana", "kiwi"]
mylists.insert(2, "watermelon")
print(mylists)      # Output: ['apple', 'banana', 'watermelon', 'kiwi']

# Extend a list by adding elements from another list
mylist1 = ["apple", "banana", "kiwi"]
mylist2 = ["watermelon", "orange"]
mylist1.extend(mylist2)
print(mylist1)      # Output: ['apple', 'banana', 'kiwi', 'watermelon', 'orange']

# Add Any Iterable:-  The extend() method does not have to append lists, 
# you can add any iterable object (tuples, sets, dictionaries etc.).
mylist = ["apple", "banana", "kiwi"]
mytuple = ("blackcurrant", "mango")
mylist.extend(mytuple)
print(mylist)      # Output: ['apple', 'banana', 'kiwi', 'blackcurrant', 'mango']

# Extend a list with characters from a string
mylist.extend("abc")
print(mylist)      # Output: ['apple', 'banana', 'kiwi', 'blackcurrant', 'mango', 'a', 'b', 'c']

# Extend a list with another list
mylist.extend(["dragnfruit", "pinaple"])
print(mylist)      # Output: ['apple', 'banana', 'kiwi', 'blackcurrant', 'mango', 'a', 'b', 'c', 'dragnfruit', 'pinaple']

# Incorrect usage: Trying to extend with an integer (will raise an error)
# mylist.extend(123)
# print(mylist)       # Output: TypeError: 'int' object is not iterable