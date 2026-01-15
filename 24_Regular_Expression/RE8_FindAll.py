import re   #The re module provides support for regular expressions in Python.

# Multi-line string containing names and ages
Nameage="""Rany is 2345 And Jeny is 65, Rany Tom is 85 and Roy is 42"""

# Corrected regex for extracting ages (only 1 or 2 digit numbers)
age = re.findall(r'\d{1,2}', Nameage)
print("Age: ", age)             # Output: Age:  ['23', '45', '65', '85', '42']

# Regex to extract names (starting with uppercase, followed by lowercase)
names = re.findall(r'[A-Z][a-z]*', Nameage)
print("Name: ", names)          # Output: Name:  ['Rany', 'And', 'Jeny', 'Rany', 'Tom', 'Roy']


text = "My birthday is on 12-05-1999 and today's date is 31-03-2025."

# Extract Only Words (Ignoring Numbers)
word = re.findall(r'[A-Za-z]+', text)
print("Words: ", word)
# Output: Words:  ['My', 'birthday', 'is', 'on', 'and', 'today', 's', 'date', 'is']

# Extract Dates in DD-MM-YYYY Format
date = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
print("Date: ", date)
# Output: Date:  ['12-05-1999', '31-03-2025']