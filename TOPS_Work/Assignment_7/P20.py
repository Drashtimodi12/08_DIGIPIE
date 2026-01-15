# 20.	Write a Python program to access alternate values between index 1 and 5 in a tuple.

# Define a tuple
mytuple = ("apple", "banana", "mango", "orange", "kiwi")

# Access alternate elements using slicing with step 2
print(mytuple[1:5:2])             # Output: ('banana', 'orange')
