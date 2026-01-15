# The re.match method in Python's re module is used to check if the beginning of a string matches a specified regular expression pattern. 
# If the pattern matches the beginning of the string, it returns a match object; otherwise, it returns None.

import re  # The re module provides support for regular expressions in Python.

text = "Rany is 2345 And Jeny is 65"

# Match "Rany" at the beginning of the text
data = re.match("Rany", text)
print(data)
# Output: <re.Match object; span=(0, 4), match='Rany'>

# Check if a match is found
if data:
    # If a match is found, print the matched string
    print("Match Found:", data.group()) 
# The match object has methods like group() to get the matched string and span() to get the start and end positions of the match. 
else:
    # If no match is found, print "No Match Found"
    print("No Match Found")


# Output: Match Found: Rany