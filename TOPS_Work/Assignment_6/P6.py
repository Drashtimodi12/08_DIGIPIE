# 6.	How to create variables in Python?

#  In Python, variables are used to store data, and you don’t need to declare their type. 
#  Python automatically assigns the data type based on the value assigned. 

# Rules for Creating Variables
# 1. Variable names must start with a letter or underscore (_).
# 2. They cannot start with a number.
# 3. They can contain letters, numbers, and underscores (_).
# 4. They are case-sensitive (name and Name are different).

# String (text)
name = 'Drashti'    
print('Name: ', name) 
print('Data type of Name: ', type(name))

# Integer (whole number)
age = 22
print('Age: ', age)
print('Data type of Age: ', type(age))

# Float (decimal number)
height = 5.4 
print('Height: ', height)
print('Data type of Height: ', type(height))

# Complex number
cn = 4+5j     
print('Number: ', cn)   
print('Data type of CN: ', type(cn))  

# Boolean (True or False)
is_stu = True
print('Is_Student: ', is_stu)
print('Data type of Is_Student: ', type(is_stu))  

# List (collection of items)
hobbies = ['coding', 'gaming', 'art']
print('Hobbies: ', hobbies)
print('Data type of Hobbies: ', type(hobbies))

# Tuple (like a list but cannot be changed)
colors = ('red', 'blue', 'green')
print('Colors:', colors)

# Dictionary (key-value pairs)
info = {'city': 'Surat', 'country': 'India'}  
print('City:', info['city'])
print('Country:', info['country'])  
print('Data type of info:', type(info))