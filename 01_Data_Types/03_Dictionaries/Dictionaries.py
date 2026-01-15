# Dictionary:- Dictionaries are written with curly brackets, and have keys and values:
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# A dictionary is a collection used to store key-value pairs. Keys must be unique. Values can be of any data type.
# can be referred to by using the key name.

# Ordered or Unordered:- 
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.
# Changeable:-      Its meaning that we can change, add or remove items after the dictionary has been created.

# Creating a dictionary with key-value pairs
mydict = {
    "fruit" : "apple",
    "Car" : "BMW",
    "num" : 10
}
print(mydict)       # Output: {'fruit': 'apple', 'Car': 'BMW', 'num': 10}


# Accessing Values Using Keys
mydict = {
    "fruit" : "apple",
    "Car" : "BMW",
    "num" : 10
}
print(mydict["Car"])        # Output: BMW

# Duplicate Keys Are Not Allowed:- If a dictionary contains duplicate keys, the last value will overwrite the previous one.
# To store multiple values for the same key, use lists or sets.
mydict = {
    "fruit" : "apple",
    "Car" : "BMW",
    "num" : 10,
    "Car" : "Honada"
}
print(mydict)       # Output: {'fruit': 'apple', 'Car': 'Honada', 'num': 10}

# Dictionary Length:- You can use len() to find the number of key-value pairs.
mydict = {
    "fruit" : "apple",
    "Car" : "BMW",
    "num" : 10
}
print(len(mydict))       # Output: 3

# Dictionary Items - Data Types:-  A dictionary can hold values of different data types.    
mydict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]        # List inside dictionary
}
print(type(mydict))        # Output: <class 'dict'>

# The dict() Constructor:- It is also possible to use the dict() constructor to make a dictionary.
mydict = dict(name = "Drashti", age = 22, citiy = "surat")
print(mydict)           # Output: {'name': 'Drashti', 'age': 22, 'citiy': 'surat'}

