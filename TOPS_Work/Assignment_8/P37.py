# 37.	Write a Python program to match a word in a string using re.match(). 

import re  # The re module provides support for regular expressions in Python.

text = "Rany is 2345 And Jeny is 65"

# Match "Rany" at the beginning of the text
data = re.match("Rany", text)

# Check if a match is found
if data:
    # If a match is found, print the matched string
    print("Match Found:", data.group()) 
# The match object has methods like group() to get the matched string and span() to get the start and end positions of the match. 
else:
    # If no match is found, print "No Match Found"
    print("No Match Found")


# Output: Match Found: Rany