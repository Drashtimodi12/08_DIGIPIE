# 25.	Write a Python program to create a dictionary of 6 key-value pairs.

# Define a dictionary with 6 key-value pairs
mydict = {
    "FName" : "Drashti",
    "LName" : "Modi",
    "Age" : "24",
    "Add" : "Surat",
    "Email" : "d@gmail.com",
    "C_No" : 9909449049
}

print(mydict)
# Output: {'FName': 'Drashti', 'LName': 'Modi', 'Age': '24', 'Add': 'Surat', 'Email': 'd@gmail.com', 'C_No': 9909449049}

# Access a value by key
print(mydict["Email"])      # Output: d@gmail.com

# Get all keys
print(mydict.keys())        # Output: dict_keys(['FName', 'LName', 'Age', 'Add', 'Email', 'C_No'])

# Get all values
print(mydict.values())      # Output: dict_values(['Drashti', 'Modi', '24', 'Surat', 'd@gmail.com', 9909449049])