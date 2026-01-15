s1 = "sun Rises in east"
s2 = " Hello Python "

# Stripping whitespace from both ends, left end, and right end
print(s2.strip())       # Output: "Hello Python"
print(s2.lstrip())      # Output: "Hello Python "
print(s2.rstrip())      # Output: " Hello Python"

# Concatenating two strings with a space in between
print(s1 + " " + s2)    # Output: "sun Rises in east Hello Python "

# Converts all to uppercase
print(s1.upper())    # Output: "SUN RISES IN EAST"

# Converts the first character of each word to uppercase
print(s1.title())    # Output: "Sun Rises In East"

# Converts the first character to uppercase and the rest to lowercase
print(s1.capitalize())  # Output: "Sun rises in east"

# Converts all to lowercase
print(s1.lower())  # Output: "sun rises in east"

# Converts all characters to lowercase, similar to lower() but more aggressive in handling special cases
print(s1.casefold())  # Output: "sun rises in east"

# Replaces "Python" with "World" in the string, preserving leading and trailing spaces
print(s2.replace("Python", "World"))  # Output: " Hello World "

# Splits the string at each occurrence of 's'
print(s1.split("s"))     # Output: ['', 'un Ri', 'e', ' in ea', 't']

# joins a list of words into a single string with spaces
words = ["Python", "is", "fun"]
print(" ".join(words))      # Output: "Python is fun"

# Joins the given string "123" with "Hello" between each character
print("Hello".join("123"))  # Output: "1Hello2Hello3"

# Searches for 'k' in the substring from index 3 to 9; returns -1 if not found
print(s1.find('k', 3, 9))  # Output: -1 (since 'k' is not present)
print(s1.find('s', 3, 9))  # Output: 5 (index of 's' in the substring)

# Searches for 'k' in the substring from index 3 to 9; raises ValueError if not found
print(s1.index('s', 3, 9))    # Output: 5 (index of 's' in the substring)
# print(s1.index('k', 3, 9))  # Output: ValueError: substring not found

# Checks if the substring from index 0 to 9 ends with 'es'
print(s1.endswith('es', 0, 9))  # Output: True

# Checks if the substring from index 0 to 2 starts with 'S'
print(s1.startswith('S', 0, 2))  # Output: False (because it's 's', not 'S')

# Returns the total number of characters in the string, including spaces
print(len(s1))  # Output: 18

# Centers the string in a field of width 27, padding it with '*'
print(s1.center(27, '*'))  # Output: "*sun Rises in east*"

# Counts the occurrences of 's' in the substring from index 0 to 7
print(s1.count('s', 0, 7))  # Output: 2

# Left justifies the string within 50 characters, padding with '*'
print(s1.ljust(50, '*'))  
# Output: "sun Rises in east*********************************"

# Splits the string into three parts: before, the matched string, and after
print(s1.partition("k"))  
# Output: ('sun Rises in east', '', '') (since 'k' is not present, the entire string is returned)








# Accessing a single character from index 4 (0-based indexing)
print(s1[4])  # Output: 'R'

# Accessing the fourth character from the end
print(s1[-4])  # Output: 'e'

# Slicing from index 4 to 9, with a step of 3
print(s1[4:9:3])  # Output: 'R ' (Characters at index 4 and 7)

# Slicing from the fourth-last to the second-last character
print(s1[-4:-1])  # Output: 'eas'




# Swaps uppercase letters to lowercase and vice versa
print("Tops".swapcase())  # Output: "tOPS"

# Checks if all characters in the string are alphanumeric (letters and numbers only)
print("abc123".isalnum())   # Output: True

# Checks if all characters in the string are alphabetic (letters only)
print('abc12'.isalpha())  # Output: False (because it contains numbers)

# Checks if all characters in the string are digits
print("212".isdigit())  # Output: True

# Checks if the string is a valid Python identifier (variable name)
print("123abc".isidentifier())  # Output: False (identifiers cannot start with a number)

# Checks if all characters are lowercase
print("Str".islower())  # Output: False (contains an uppercase letter)

# Checks if the first letter of each word is uppercase (Title Case)
print("Tbc".istitle())  # Output: True

# Checks if all characters are uppercase
print("ABC".isupper())  # Output: True
