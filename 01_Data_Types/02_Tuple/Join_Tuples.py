# Join Two Tuples:- To join two or more tuples you can use the + operator
t1 = ("1", "apple", "2", "banana")
t2 = ("3", "red", "4", "yellow")
t3 = t1 + t2
print(t3)
# Output: ('1', 'apple', '2', 'banana', '3', 'red', '4', 'yellow')

# Multiply Tuples:- If you want to multiply the content of a tuple a given number of times, you can use the * operator
t1 = ("1", "apple", "2", "banana")
t2 = t1 * 2
print(t2)
# Output: ('1', 'apple', '2', 'banana', '1', 'apple', '2', 'banana')

# Nested Tuple Joining:- You can create a nested tuple instead of merging elements.
t1 = ("1", "apple", "2", "banana")
t2 = ("3", "red", "4", "yellow")
t3 = (t1, t2)
print(t3)
# Output: (('1', 'apple', '2', 'banana'), ('3', 'red', '4', 'yellow'))