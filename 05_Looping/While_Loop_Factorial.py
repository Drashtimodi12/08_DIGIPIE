# Factorial calculation using while loop : 5!=5*4*3*2*1=120

num = 5  # Store the original number
fact = 1  # Initialize factorial result

number = num  # Use a separate variable for the loop

while number > 0:  # Loop runs until number becomes 0
    fact *= number  # Multiply fact by the current number
    number -= 1     # Decrement the number by 1

# Using f-string
print(f"Factorial of {num} is {fact}")  # Output: Factorial of 5 is 120