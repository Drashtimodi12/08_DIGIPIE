# Join Two Lists:- There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.
l1 = ["apple", "banana"]
l2 = ["kiwi", "grapes", "orange"]
l3 = l1 + l2
print(l3)       # Output: ['apple', 'banana', 'kiwi', 'grapes', 'orange']

# append():- Another way to join two lists is by appending all the items from list2 into list1, one by one:
l1 = ["1", "2", "3"]
l2 = ["a", "b", "c", "d"]
for x in l2 :
    l1.append(x)
print(l1)       # Output: ['1', '2', '3', 'a', 'b', 'c', 'd']

# extend():- where the purpose is to add elements from one list to another list:
l1 = ["1", "2", "3"]
l2 = ["a", "b", "c", "d"]
l1.extend(l2)
print(l1)       # Output: ['1', '2', '3', 'a', 'b', 'c', 'd']