# Removing Items:- There are several methods to remove items from a dictionary:

# pop() method removes the item with the specified key name
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
student.pop("Add")
print(student)      # Output: {'Name': 'Drashti', 'Age': 21, 'Contact': 9909449049}


# popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
student.popitem()
print(student)      # Output: {'Name': 'Drashti', 'Age': 21, 'Add': 'Surat'}




# del keyword removes the item with the specified key name:
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
del student["Contact"]
print(student)      # Output: {'Name': 'Drashti', 'Age': 21, 'Add': 'Surat'}

# The del keyword can also delete the dictionary completely:
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
del student
# print(student)      # this will cause an error because "student" no longer exists.



# clear() method empties the dictionary:
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
student.clear()
print(student)      # Output: {}
