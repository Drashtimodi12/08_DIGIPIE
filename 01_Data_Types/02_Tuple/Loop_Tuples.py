# Looping Through a Tuple in Python:- Tuples are ordered, immutable collections that allow duplicate values. 
# You can iterate through a tuple using different methods.

# 1.    You can loop through the tuple items by using a for loop.
mytuple = ("apple", "banana", "strawberry", "raspberry")      
for i in mytuple :
    print(i)
# Output:   apple
#           banana
#           strawberry
#           raspberry

# You can also iterate through a tuple using indexes with the range() and len() functions.
mytuple = ("cherry", "strawberry", "raspberry")      
for i in range(len(mytuple)) :
    print(mytuple[i])
# Output:   cherry
#           strawberry
#           raspberry


# 2.    You can loop through the tuple items by using a while loop.
# Use the len() function to determine the length of the tuple, 
# then start at 0 and loop your way through the tuple items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.
mytuple = ("apple", "banana", "cherry")      
i = 0
while i <len(mytuple) :
    print(mytuple[i])
    i = i + 1
# Output:   apple
#           banana
#           cherry

# Using enumerate() to Get Index and Value:- If you need both index and value, use enumerate().
# Looping Through a Nested Tuple:- If a tuple contains another tuple inside it, use nested loops.