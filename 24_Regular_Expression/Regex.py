"""
Regex (Regular Expression) is a tool used to search, match, extract, and manipulate patterns from text.
Think of regex like a smart search filter that can find exactly what you want inside a string.

Always import regex module first: import re
Use r"" (raw string) to avoid escaping issues: r"\d+"

Simple Real-Life Examples
    Text: "My phone number is 9876543210"
    Regex: \d{10} → matches 9876543210 (all 10 digits)

    
Why use Regex?
    Validate emails, phone numbers, passwords
    Search for patterns in text
    Replace or extract text
    Split text based on patterns

Symbol	: Meaning
^ :	starts with
$ :	ends with
. :	Matches any character except newline
* :	repeat 0 or more times
+ :	repeat 1 or more times
? :	optional / 0 or 1 repetition
{n} :	repeat exactly n times
{n,} : At least n times
{n,m} :	repeat n to m times / Between n and m times
[] : Character set
[^] : Not in set
() : Grouping
\ : Escape special characters
\d :	digit (0–9)
\D :	non-digit [^\d]
\w :	word character (A–Z, a–z, 0–9, _)
\W :	non-word character
\s :	whitespace (space, tab)
\S : Non-whitespace
\b : Word boundary	
\B : Not word boundary
"""

import re

# ^ → string must start with
# \+91 → literal +91
# \d{10} → exactly 10 digits
# $ → string must end there
pattern = r"^\+91\[0-9]{10}$"

mystring = input("Enter your number: ")
x = re.match(pattern, mystring)

if x:
    print("Valid number")
else:
    print("Invalid number")
# op:
# Enter your number: 9909449049
# Invalid number