# sort():- Sorting a list alphabetically, ascending, by default:
mylist = ["orange", "mango", "kiwi", "pineapple", "banana"]
mylist.sort()
print(mylist)       # Output: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# Sort Descending:- To sort descending, use the keyword argument reverse = True:
mylist.sort(reverse = True)
print(mylist)       # Output: ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

# Sorting numbers in ascending order
mylist = [100, 50, 77, 97, 45, 23]
mylist.sort()
print(mylist)       # Output: [23, 45, 50, 77, 97, 100]

# Sorting numbers in descending order
mylist.sort(reverse = True)
print(mylist)       # Output: [100, 97, 77, 50, 45, 23]


# Case Insensitive Sort:- By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
# Case sensitive sorting can give an unexpected result:
mylist = ["banana", "Orange", "Kiwi", "cherry"]
mylist.sort()
print(mylist)       # Output: ['Kiwi', 'Orange', 'banana', 'cherry']

# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use str.lower as a key function:
# Perform a case-insensitive sort of the list:
mylist = ["banana", "Orange", "Kiwi", "cherry"]
mylist.sort(key = str.lower)
print(mylist)       # Output: ['banana', 'cherry', 'Kiwi', 'Orange']

# reverse():- The reverse() method reverses the current sorting order of the elements.
mylist = ["banana", "Orange", "Kiwi", "cherry"]
mylist.reverse()
print(mylist)       # Output: ['cherry', 'Kiwi', 'Orange', 'banana']