# 35.	Write a Python program to match a word in a string using re.match(). 

import re  # The re module provides support for regular expressions in Python.

text = "Rany is 2345 And Jeny is 65"

# Match "Rany" at the beginning of the text
data = re.match("Rany", text)
print(data)
# Output: <re.Match object; span=(0, 4), match='Rany'>