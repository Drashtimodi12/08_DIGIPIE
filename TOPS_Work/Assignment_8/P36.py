# 36.	Write a Python program to search for a word in a string using re.search(). 

import re  # The re module provides support for regular expressions in Python.

text = "Rany is 2345 And Jeny is 65"

# Search for "Rany" anywhere in the text
data = re.search("Rany", text)

# Check if a match is found
if data:
    # If a match is found, print the matched string
    print("Match Found:", data.group())  
else:
    # If no match is found, print "No Match Found"
    print("No Match Found")

# Output: Match Found: Rany