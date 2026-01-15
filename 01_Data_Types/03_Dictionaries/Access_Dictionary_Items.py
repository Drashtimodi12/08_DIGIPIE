# Accessing Items:- You can access the items of a dictionary by referring to its key name, inside square brackets:

student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
# Access using key
print(student["Age"])       # Output: 21




# There is also a method called get() that will give you the same result:
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : [9909449049, 9979849049]
}
print(student.get("Name"))       # Output: Drashti
print(student["Contact"][1])       # Output: 9979849049
# print(student("Email"))         # Output: None (No error, unlike student["Email"])


# Get Keys:- The keys() method will return a list of all the keys in the dictionary.
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : [9909449049, 9979849049]
}
print(student.keys())       # Output: dict_keys(['Name', 'Age', 'Add', 'Contact'])

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Contact" : [9909449049, 9979849049]
}
#before the change
print(student.keys())       # Output: dict_keys(['Name', 'Age', 'Contact'])
student["Add"] = "Surat"
#after the change
print(student.keys())       # Output: dict_keys(['Name', 'Age', 'Contact', 'Add'])





# Get Values:- The values() method will return a list of all the values in the dictionary.
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : [9909449049, 9979849049]
}
print(student.values())       # Output: dict_values(['Drashti', 21, 'Surat', [9909449049, 9979849049]])

# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Contact" : [9909449049, 9979849049]
}
#before the change
print(student.values())       # Output: dict_values(['Drashti', 21, [9909449049, 9979849049]])
student["Add"] = "Surat"
#after the change
print(student.values())       # Output: dict_values(['Drashti', 21, [9909449049, 9979849049], 'Surat'])





# Get Items:- The items() method will return each item in a dictionary, as tuples in a list.
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
print(student.items())       # Output: dict_items([('Name', 'Drashti'), ('Age', 21), ('Add', 'Surat'), ('Contact', 9909449049)])

# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
#before the change
print(student.items())       # Output: dict_items([('Name', 'Drashti'), ('Age', 21), ('Add', 'Surat'), ('Contact', 9909449049)])
student["Year"] = 2004
#after the change
print(student.items())       # Output: dict_items([('Name', 'Drashti'), ('Age', 21), ('Add', 'Surat'), ('Contact', 9909449049), ('Year', 2004)])




# Check if Key Exists:- To determine if a specified key is present in a dictionary use the in keyword:
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
if "Add" in student :
    print("Yes, 'Add' is one of the keys in the thisdict dictionary")
    # Output: Yes, 'Add' is one of the keys in the thisdict dictionary