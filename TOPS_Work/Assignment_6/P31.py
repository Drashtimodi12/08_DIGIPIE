# 31.	Write a Python program that manipulates and prints strings using various string methods.

# Define a string
text = "  Hello, Python World!  "       

# strip(): Removes leading and trailing whitespaces.
print("Stripped text:", text.strip())   # Output: Stripped text: Hello, Python World!

# upper(): Converts the string to uppercase.
print("Uppercase text:", text.upper())  # Output: Uppercase text:   HELLO, PYTHON WORLD!

# lower(): Converts the string to lowercase.
print("Lowercase text:", text.lower())      # Output: Lowercase text:   hello, python world!

# replace(old, new): Replaces all occurrences of old with new.
print("Replaced text:", text.replace("Python", "Java"))     # Output: Replaced text:   Hello, Java World! 

# split(): Splits the string into a list of words.
print("Splitted text:", text.split())       # Output: Splitted text: ['Hello,', 'Python', 'World!']

# startswith(substring): Checks if the string starts with the given substring.
print("Starts with 'Hello':", text.startswith("Hello"))     # Output: Starts with 'Hello': False

# endswith(substring): Checks if the string ends with the given substring.
print("Ends with 'World!':", text.endswith(" "))        # Output: Ends with 'World!': True

# find(substring): Returns the index of the first occurrence of the substring or -1 if not found.
print("Position of 'Python':", text.find("Python"))     # Output: Position of 'Python': 9

# count(substring): Counts the number of occurrences of the substring.
print("Count of 'Python':", text.count("Python"))       # Output: Count of 'Python': 1

# capitalize(): Capitalizes the first letter of the string.
print("Capitalized text:", text.capitalize())       # Output: Capitalized text:   hello, python world!  

# center(width, char): Centers the string within a field of the specified width, padded with the specified character.
print("Centered text:", text.center(40, '*'))       # Output: Centered text: ********  Hello, Python World!  ********

# isalnum(): Checks if all characters in the string are alphanumeric.
print("Is alphanumeric:", text.isalnum())       # Output: Is alphanumeric: False

# isalpha(): Checks if all characters in the string are alphabetic.
print("Is alphabetic:", text.isalpha())     # Output: Is alphabetic: False

# isdigit(): Checks if all characters in the string are digits.
print("Is digit:", text.isdigit())      # Output: Is digit: False