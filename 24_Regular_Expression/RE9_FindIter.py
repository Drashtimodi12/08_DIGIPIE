# The re.finditer method in Python's re module returns an iterator yielding match objects for all non-overlapping matches 
# of the pattern in the string. Each match object can be used to get information about the match, such as the matched 
# text and its position in the string.


import re  # The re module provides support for regular expressions in Python.

text = "Python is world's best programming language"

# Use re.finditer to find all occurrences of the pattern "world's" in the text
for match in re.finditer("world's", text) :
    # If a match is found, print the matched text
    print("Match Text: ", match.group())    # Output: Match Found: world's

    # Print the position of the matched text in the form of a tuple (start, end)
    print("Position:", match.span())  # Output: (11, 18)