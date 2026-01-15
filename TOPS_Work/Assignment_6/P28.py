# 28.	Write a Python program to skip 'banana' in a list using the continue statement. List1 = ['apple', 'banana', 'mango']

# Define the list
list1 = ['Apple', 'Banana', 'Mango']

# Loop through the list and skip 'banana' using continue    
for i in list1 :
    if i == 'Banana' :
        continue     # Skip 'banana' and move to the next item
    print(i) 