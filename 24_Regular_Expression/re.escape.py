# re.escape(string)
# Purpose: Escapes all special regex characters in a string.
# Useful if you want to match literal text.
# This is useful when your string contains characters like:
# . ^ $ * + ? { } [ ] \ | ( )


import re

# mystr = "Hello. How are you? (Good)"
# pattern = re.escape(mystr)
# print(pattern)      # OP: Hello\. How\ are\ you\?\ \(Good\)



text = "file.txt"
pattern = re.escape(text)  # becomes "file\.txt"
print(pattern)
result = re.search(pattern, "my file.txt backup")
print(result.group())

# OP:
# file\.txt
# file.txt