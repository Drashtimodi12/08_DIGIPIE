# Join Sets:- There are several ways to join two or more sets in Python.
# Both union() and update() will exclude any duplicate items.

# 1.    Union():- The union() method returns a new set with all items from both sets. We can also usE with different data types.
s1 = {"java", "python", "php", "html"}
s2 = {"a", "b", "c"}
s4 = s1.union(s2)
print(s4)       # Output: {'php', 'c', 'java', 'python', 'a', 'b', 'html'}

# Join Multiple Sets:- All the joining methods and operators can be used to join multiple sets.
# When using a method, just add more sets in the parentheses, separated by commas:
s1 = {"java", "python", "php", "html"}
s2 = {"a", "b", "c"}
s3 = {"apple", True, "banana"}
s5 = s1.union(s1, s2, s3)
print(s5)       # Output: {'apple', True, 'java', 'python', 'banana', 'html', 'php', 'c', 'a', 'b'}

# Using | (Pipe) Operator:- The | operator performs the same operation as union() but is shorter and more readable.
# The |(pipe) operator only allows you to join sets with sets, and not with other data types like you can with the union() method.
s1 = {"hp", "lenov", "dell"}
s2 = {"200", "87", "64"}
s3 = s1 | s2
print(s3)       # Output: {'dell', '64', '200', 'hp', '87', 'lenov'}

# When using the | operator, separate the sets with more | operators:
s1 = {"hp", "lenov", "dell"}
s2 = {"200", "87", "64"}
s3 = {"saree", "kurta", "coatset"}
s4 = s1 | s2 | s3
print(s4)       # Output: {'dell', 'kurta', '200', 'hp', '87', 'lenov', 'coatset', 'saree', '64'}

# Joining Sets with Other Data Types:- The union() method allows you to join a set with other data types, like lists or tuples.
# The result will be a set.
# union() allows joining different data types (like lists & tuples), where as | only works with sets.
set1 = {"BMW", "Alto", "Honda"}
tuple1 = (1, 2, 3)
x = set1.union(tuple1)
print(x)        # Output: {1, 'Alto', 2, 'Honda', 3, 'BMW'}



# 2.    Update():- The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.
s1 = {"200", "87", "64"}
s2 = {"saree", "kurta", "coatset"}
s1.update(s2)
print(s1)       # Output: {'saree', '87', '64', 'coatset', 'kurta', '200'}



# 3.    Intersection:- Keep ONLY the duplicates. We can also use with different data types.
# The intersection() method returns a new set containing elements common to both sets. 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)     # Output: {'apple'}

# Intersection with Boolean Values:- In Python, True is treated as 1 and False is treated as 0 when working with sets.
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)     # Output: {False, 1, 'apple'}

# Using & Operator (Shorthand):- The & operator works as a shortcut for intersection(), but it only works with sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)     # Output: {'apple'}


# 4.    The intersection_update() method modifies the original set to keep only common elements. We can also use with different data types.
# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)     # Output: {'apple'}

set1 = {100, 200, 300, 10, 20, 30}
set2 = {10, 20, 30, 40}
set1.intersection_update(set2)
print(set1)         # Output: {10, 20, 30}



# 5.    Difference:- The difference() method will return a new set that will contain only the items from the 
# first set that are not present in the other set. We can also us ewith different data types.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)         # Output: {'banana', 'cherry'} 
set4 = set2.difference(set1)
print(set4)         # Output: {'google', 'microsoft'}

# You can use the - operator instead of the difference() method, and you will get the same result.
# The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.
set1 = {100, 200, 300, 10, 20, 30}
set2 = {10, 20, 30, 40}
set3 = set1 - set2
print(set3)         # Output: {200, 100, 300}



# 6.    The difference_update() method will also keep the items from the first set that are not in the other set, 
# but it will change the original set instead of returning a new set.
s1 = {10, 20, 30, 40}
s2 = {100, 200, 300, 10, 20, 30}
s1.difference_update(s2)
print(s1)         # Output: {40}



# 7.    Symmetric Differences:= It will keep only the elements that are NOT present in both sets.
# The symmetric_difference() method keeps all items EXCEPT the duplicates.
s1 = {10, 20, 30, 40}
s2 = {100, 200, 300, 10, 20, 30}
s3 = s1.symmetric_difference(s2)
print(s3)       # Output: {40, 100, 200, 300}

# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
# The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)         # Output: {'banana', 'cherry', 'microsoft', 'google'}


# 8.    The symmetric_difference_update() method will also keep all but the duplicates, but it will change the 
# original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple", "Windos"}
set1.symmetric_difference_update(set2)
print(set1)         # Output: {'banana', 'cherry', 'microsoft', 'Windos', 'google'}



# 9.    isdisjoint():- Returns whether two sets have a intersection or not 
# Returns True → if the sets have no common elements.
# Returns False → if there is at least one common element.
s1 = {10,20,30}
s2 = {100,200,300}
print(s1.isdisjoint(s2))        # Output: True

# 10.   issubset():- <= Returns whether another set contains this set or not (s1 all item in s2 than print True)
# < Returns whether all items in this set is present in other, specified set(s)
# Returns True → if all elements of s1 exist in s2.
# Returns False → if at least one element of s1 is missing from s2.
s1 = {10,20,30}
s2 = {100,200,10,20}
print(s1.issubset(s2))          # Output: False

# 11.   issuperset():- >= Returns whether this set contains another set or not
# > Returns whether all items in other, specified set(s) is present in this set
# Returns True → if all elements of s2 exist in s1.
# Returns False → if at least one element of s2 is missing from s1.
s1 = {10,20}
s2 = {10,20,30}
print(s2.issuperset(s1))        # Output: True