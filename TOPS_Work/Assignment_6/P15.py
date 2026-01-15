# 15.	Write a Python program to find a specific string in the list using a simple for loop and if condition.

# Define the list
list1 = ['Apple', 'Banana', 'Mango']
search_string = input("Enter the string to search for: ")

# Loop through the list and check if the string matches
found = False  # Flag to track if the string is found
for i in list1:
    if i == search_string:
        found = True
        break

# Output the result 
if found:
    print(f"{search_string} is found in the list.")
else:
    print(f"{search_string} is not found in the list.")
