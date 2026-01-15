# Open Terminal Press Ctrl + ~
# Check the directory where your file is saved.
# Use the cd command to change directories. cd .\Basic\
# Ex: cd C:\PYTHON_PROGRAM\PYTHON_CLASS_WORK\Basic
# If you need to move back a folder, use: cd ..
# Run: Once you're inside the correct folder, run the program with:  py .\Hello.py

# Printing simple text messages
print ('Hello Python')  # Single quotes, Output: Hello Python
print("Hello Python!")  # Double quotes, Output: Hello Python!

# Printing multi-line text using triple quotes
print("""Hello Everyone!
Wellcome""")
# Output: Hello Everyone!
# Wellcome

# Printing with single and double quotes inside the string
print("Hello ' Python! '")   # Single quotes inside double quotes, Output: Hello ' Python! '
print('Hello " Python! "')   # Double quotes inside single quotes, Output: Hello " Python! "

# Using escape characters to include quotes
print("Hello \" Python! \"")    # Escaping double quotes, Output: Hello " Python! "
print('Hello \' Python! \'')    # Escaping single quotes, Output: Hello ' Python! '

# Using escape characters to include backslashes
print("Hello \\ Python! \\")    # Escaping backslashes, Output: Hello \ Python! \

# Printing with special characters
print("Hello \ Python! \ ")     # Single backslash before spaces, Output: Hello \ Python! \
print("Hello \n Wellcome")      # New line character, Output: Hello
                                    # Wellcome

print("Hello \t Wellcome")      # Tab space, Output: Hello        Wellcome
print("Hello!\b Python!")       # Backspace, Output: Hello Python!
print("Hello \\\" Python! \"")  # Escaping backslash and double quotes, Output: Hello \" Python! "

# Print with end and separator
print("hello",end=" ")  # Prints 'hello' without a newline, adding a space instead
print("python")     # Output: hello python

print("python","java","php","node",sep=" ")     # Prints with space separator, Output: python java php node
print("python","java","php","node",sep=" | ")   # Prints with '|' separator, Output: python | java | php | node