# 31.	Write a Python program to convert two lists into one dictionary using a for loop. 

# Define two lists
keylist = ["Name", "Add", "C_No"]
valuelist = ["Sejal", "Surat", "0922343323"]

# Create an empty dictionary
mydict = {}

# Loop to merge the lists into a dictionary
for i in range(len(keylist)) :
    mydict[keylist[i]] = valuelist[i]

print(mydict)       # Output: {'Name': 'Sejal', 'Add': 'Surat', 'C_No': '0922343323'}