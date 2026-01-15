# Understanding the filter() function:- The filter() function is used to filter out elements from an iterable based on a 
# condition defined in a function. It only includes elements where the function returns True.
# filter() functions return True or False


l = ["Python", "Java", "Php", "HTML"]

def isvalid(word) :
    if word.startswith("P") :       # Check if the word starts with 'P'
        return word            # Returns the value if the condition is True

# Your function isvalid() should return True instead of returning the word itself.
k = filter(isvalid, l)      # Filters elements from the list 'i' based on 'isValid'
print(list(k))          # Convert the filtered result to a list and print it
# Output: ['Python', 'Php']




# Alternative Approach (Using Lambda Function):- A shorter way to achieve the same result:
k = filter(lambda word : word.startswith("P"), l)     
print(list(k))  
# Output: ['Python', 'Php']




# Filtering Odd Numbers from a List
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

c = filter(lambda x: x % 2 != 0, l)  # Keep only odd numbers
print(list(c))      # Output: [1, 3, 5, 7, 9]




# Filtering Perfect Squares
from math import sqrt

data = [1, 4, 6, 8, 9, 10, 12, 16, 81, 23, 36]  

def isPreSquare(i):
    return sqrt(i).is_integer()     # Check if square root is a whole number

k = filter(isPreSquare,data)
print(list(k))          # Output: [1, 4, 9, 16, 81, 36]