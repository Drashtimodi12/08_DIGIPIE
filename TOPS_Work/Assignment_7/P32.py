# 32.	Write a Python program to count how many times each character appears in a string.

# Input string
text = "hello world"

# Create an empty dictionary
char_count = {}

# Count character occurrences
for char in text:
    char_count[char] = char_count.get(char, 0) + 1

# Print results
for char, count in char_count.items():
    print(f"'{char}': {count}")

# Output:
# 'h': 1
# 'e': 1
# 'l': 3
# 'o': 2
# ' ': 1
# 'w': 1
# 'r': 1
# 'd': 1