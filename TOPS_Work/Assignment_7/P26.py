# 26.	Write a Python program to access values using keys from a dictionary.

# Define a dictionary key-value pairs
mydict = {
    "FName" : "Drashti",
    "LName" : "Modi",
    "Age" : "24",
    "Add" : "Surat",
    "Email" : "d@gmail.com",
    "C_No" : 9909449049
}

# Access values using dictionary keys
print("First Name: ", mydict["FName"])        # Output: First Name:  Drashti
print("Last Name: ", mydict["LName"])         # Output: Last Name:  Modi
print("Age: ", mydict["Age"])                 # Output: Age:  24
print("Address: ", mydict["Add"])             # Output: Address:  Surat
print("Email: ", mydict["Email"])             # Output: Email:  d@gmail.com 

# Alternative method: Using get()
print("Contact: ", mydict.get("C_No"))       # Output: Contact:  9909449049