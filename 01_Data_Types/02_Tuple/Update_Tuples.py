# Change Tuple Values:- Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

t = ("apple", "banana", "kiwi", "orange")
l = list(t)
l[1] = "mango"
t = tuple(l)
print(t)        # Output: ('apple', 'mango', 'kiwi', 'orange')

# Add Items:- Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
# 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
t = ("apple", "banana", "kiwi", "orange")
l.append("grapes")      
t = tuple(l)
print(t)        # Output: ('apple', 'banana', 'kiwi', 'orange', 'grapes')

# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
t = ("apple", "banana", "kiwi", "orange")
y = ("grapes",)
t += y
print(t)        # Output: ('apple', 'banana', 'kiwi', 'orange', 'grapes')


# Remove Items:- You cannot remove items in a tuple.
# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
t = ("apple", "banana", "kiwi", "orange")
l = list(t)
l.remove("apple")
t = tuple(l)
print(t)        # Output: ('banana', 'kiwi', 'orange')

# Or you can delete the tuple completely:
# The del keyword can delete the tuple completely:
t = ("java", "php", "html")
del t
print(t)        #this will raise an error because the tuple no longer exists