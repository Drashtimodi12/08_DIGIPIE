# Factorial calculation using for loop : 5!=5*4*3*2*1=120 

number = int(input("Enter a number: "))  # Taking user input
fact = 1

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(number, 0, -1):  # Loop from number to 1
        fact *= i  # Multiply fact by i

# Using f-string
print(f"Factorial of {number} is {fact}")

# Output:
# Enter a number: 5
# Factorial of 5 is 120

print("\n======================================\n")



# Input a number and calculate its factorial using a loop.
a = int(input("Enter number: "))
m = 1
for i in range(1, a+1):
    m *= i
print(m)
# OP:
# Enter number: 5
# 120