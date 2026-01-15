# The re.search method in Python's re module is used to search for a pattern anywhere in the string. 
# If the pattern is found, it returns a match object; otherwise, it returns None.

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