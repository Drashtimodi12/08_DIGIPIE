# Break in While Loop
# Ask the user to guess a secret number (e.g., 7).
# Keep looping until the user guesses correctly using while.
# Stop immediately using break.


while True:
    num = int(input("Guess the number: "))
    if num == 7:
        print("Congratulations! You guessed it correctly.")
        break
    else:
        print("Guess another number: ")

# OP:
# Guess the number: 4
# Guess another number: 
# Guess the number: 6
# Guess another number: 
# Guess the number: 7
# Congratulations! You guessed it correctly.