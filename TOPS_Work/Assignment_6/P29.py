# 29.	Write a Python program to stop the loop once 'banana' is found using the break statement.

# Define the list
list1 = ['Apple', 'Banana', 'Mango']

# Loop through the list and skip 'banana' using continue    
for i in list1 :
    if i == 'Banana' :
        break  # Stop the loop once 'Banana' is found    
    print(i) 