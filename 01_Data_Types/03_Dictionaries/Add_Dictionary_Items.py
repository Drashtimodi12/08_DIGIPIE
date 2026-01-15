# Adding Items:- Adding an item to the dictionary is done by using a new index key and assigning a value to it:
student = {
    "Name" : "Drashti",
    "Add" : "Surat",
    "Contact" : 9909449049
}
student["Email"] = "drashti@gmail.com"
print(student)      # Output: {'Name': 'Drashti', 'Add': 'Surat', 'Contact': 9909449049, 'Email': 'drashti@gmail.com'}



# Update Dictionary:- The update() method will update the dictionary with the items from a given argument. If the 
# item does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs.
student = {
    "Name" : "Drashti",
    "Add" : "Surat",
    "Contact" : 9909449049
}
student.update({"Age" : 22})
print(student)       # Output: {'Name': 'Drashti', 'Age': 22, 'Add': 'Surat', 'Contact': 9909449049}

# Updating a Dictionary Value
# Appending to a List in Dictionary
student["Address"] = ["Baroda", "Surat"]
print(student)      
# Output: {'Name': 'Drashti', 'Add': 'Surat', 'Contact': 9909449049, 'Age': 22, 'Address': ['Baroda', 'Surat']}

student["Address"].append("Amd")
print(student)
# Output: {'Name': 'Drashti', 'Add': 'Surat', 'Contact': 9909449049, 'Age': 22, 'Address': ['Baroda', 'Surat', 'Amd']}