# Change Values:- You can change the value of a specific item by referring to its key name:
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
student["Age"] = 22       
print(student)              # Output: {'Name': 'Drashti', 'Age': 22, 'Add': 'Surat', 'Contact': 9909449049}
print(student["Age"])       # Output: 22




# Update Dictionary:- The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
student.update({"Name" : "Sejal"})
print(student)       # Output: {'Name': 'Sejal', 'Age': 21, 'Add': 'Surat', 'Contact': 9909449049, 'Year': 2004}