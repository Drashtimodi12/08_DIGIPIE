# Updating List Items

# Change a specific item in the list, refer to the index number
mylist = ["apple", "banana", "kiwi"]
mylist[2] = "cherry"    # Replacing 'kiwi' with 'cherry'
print(mylist)       # Output: ['apple', 'banana', 'cherry']

# Change a Range of Item Values:-  it define a list with the new values, 
# and refer to the range of index numbers where you want to insert the new values
mylist = ["apple", "banana", "kiwi", "orange", "pinaple"]
mylist[1:3] = ["watermelon", "mango"]       # Replacing 'banana' and 'kiwi' with new values
print(mylist)       # Output: ['apple', 'watermelon', 'mango', 'orange', 'pinaple']

# Change the second value by replacing it with two new values:
mylist[1:2] = ["blackcurrant", "Kiwi"]
print(mylist)       # Output: ['apple', 'blackcurrant', 'Kiwi', 'mango', 'orange', 'pinaple']

# Change the second and third value by replacing it with one value:
mylist[1:3] = ["watermelon"]
print(mylist)       # Output: ['apple', 'watermelon', 'mango', 'orange', 'pinaple']


# Inserting Items into a List
# Use insert() to add an item at a specific position without replacing existing values
mylists = ["apple", "banana", "kiwi"]
mylists.insert(2, "watermelon")     # Insert 'watermelon' at index 2
print(mylists)      # Output: ['apple', 'banana', 'watermelon', 'kiwi']