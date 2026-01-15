# Unpacking a Tuple:- When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
mytuple = ("apple", "banana", "cherry")         # Packing a tuple
(green, red, yellow) = mytuple                  # Unpacking the tuple into variables
print(green)
print(red)
print(yellow)
# Output: apple
#         banana
#         cherry

# Unpacking with Asterisk(*):- When we have more values than variables, we use * to collect multiple values into a list.
mytuple = ("apple", "banana", "cherry", "strawberry", "raspberry")      
green, red, *yellow = mytuple
print(green)
print(red)
print(yellow)
# Output:-  apple
#           banana
#           ['cherry', 'strawberry', 'raspberry']

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until 
# the number of values left matches the number of variables left.
mytuple = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *red, yellow) = mytuple
print(green)
print(red)
print(yellow)
# Output:-  apple
#           ['banana', 'cherry', 'strawberry']
#           raspberry

# Tuple unpacking is commonly used to swap two variables without using a temporary variable.
a = 10
b = 20
a, b = b, a     # Swapping values
print(a)  
print(b)  
# Output: 20
#         10