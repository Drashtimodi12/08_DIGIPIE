# 39.	Write a Python program to test whether a passed letter is a vowel or not. 

# Taking user input
letter = input("Enter a letter: ").lower()  # Convert input to lowercase for case insensitivity

# List of vowels
vowels = "aeiou"

# Checking if the letter is a vowel
if letter in vowels and len(letter) == 1:
    print(f"'{letter}' is a vowel.")
else:
    print(f"'{letter}' is not a vowel.")
