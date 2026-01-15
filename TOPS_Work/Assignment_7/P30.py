# 30.	Write a Python program to separate keys and values from a dictionary using keys() and values() methods. 

# Define a dictionary key-value pairs
mydict = {
    "FName" : "Drashti",
    "LName" : "Modi",
    "Age" : "24",
    "Add" : "Surat",
    "Email" : "d@gmail.com",
    "C_No" : 9909449049
}

# Print the keys
print(mydict.keys())        # Output: dict_keys(['FName', 'LName', 'Age', 'Add', 'Email', 'C_No'])

# Print the values
print(mydict.values())      # Output: dict_values(['Drashti', 'Modi', '24', 'Surat', 'd@gmail.com', 9909449049])