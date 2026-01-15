# Loop Through a Dictionary:- You can loop through a dictionary by using a for loop. When looping through a dictionary, 
# the return value are the keys of the dictionary, but there are methods to return the values as well.

# Print all key names in the dictionary, one by one:
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
for k in student :
    print(k)
# Output:
# Name
# Age
# Add
# Contact

# You can use the keys() method to return the keys of a dictionary:
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
for k in student.keys() :
    print(k)
# Output:
# Name
# Age
# Add
# Contact

student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
for key in student :
    print(key)
# Output:
# Name
# Age
# Add
# Contact





# Print all values in the dictionary, one by one:
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
for k in student :
    print(student[k])
# Output:
# Drashti
# 21
# Surat
# 9909449049

# You can also use the values() method to return values of a dictionary:
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
for value in student.values() :
    print(value)
# Output:
# Drashti
# 21
# Surat
# 9909449049




# Loop through both keys and values, by using the items() method:
student = {
    "Name" : "Drashti",
    "Age" : 21,
    "Add" : "Surat",
    "Contact" : 9909449049
}
for key, value in student.items() :
    print(key, value)
# Output:
# Name Drashti
# Age 21
# Add Surat
# Contact 9909449049