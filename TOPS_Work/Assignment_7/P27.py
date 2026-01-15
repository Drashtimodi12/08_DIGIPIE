# 27.	Write a Python program to update a value in a dictionary.

# Define a dictionary key-value pairs
mydict = {
    "FName" : "Drashti",
    "LName" : "Modi",
    "Age" : "24",
    "Add" : "Surat",
    "Email" : "d@gmail.com",
    "C_No" : 9909449049
}

# Update a value using direct assignment
# mydict.update({"FName" : "Sejal"})
mydict["FName"] = "Sejal" 

# Print the updated first name separately
print(mydict["FName"])      # Output: Sejal

print(mydict)       # Output: {'FName': 'Sejal', 'LName': 'Modi', 'Age': '24', 'Add': 'Surat', 'Email': 'd@gmail.com', 'C_No': 9909449049}