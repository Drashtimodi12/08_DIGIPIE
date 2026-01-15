# Armstrong numbers:= 153=1*1*1=1
# 5=5*5*5=125
# 3=3*3*3=27
# 1+125+27=153


# Loop through all 3-digit numbers (100 to 999)
# Extract individual digits
for i in range(100,1000) :

    a = i // 100  # First digit (hundreds place)
    b = (i // 10) % 10  # Second digit (tens place)
    c = i % 10  # Third digit (ones place)

    # Calculate sum of cubes of digits
    armstrong_sum = (a ** 3) + (b ** 3) + (c ** 3)

    # Check if the number is an Armstrong number
    if i == armstrong_sum:
        print(i, "is an Armstrong Number")
# OP:
# 153 is an Armstrong Number
# 370 is an Armstrong Number
# 371 is an Armstrong Number
# 407 is an Armstrong Number

print("\n------------------------\n")





# Loop through numbers from 100 to 999 (3-digit numbers)
for i in range(100, 1000):  
    number = i  # Store the original number
    temp = number  # Keep a copy for later comparison
    sum = 0  # Initialize sum to store the sum of cubes of digits

    # Extract digits and calculate the sum of their cubes
    while number != 0:  
        rem = number % 10  # Get the last digit
        sum += rem * rem * rem  # Add the cube of the digit to sum
        number = number // 10  # Remove the last digit

    # Check if the number is an Armstrong number
    if temp == sum:  
        print(temp, ': is an Armstrong Number.')  # Print Armstrong number
    else:  
        pass  # Skip non-Armstrong numbers
# OP:
# 153 : is an Armstrong Number.
# 370 : is an Armstrong Number.
# 371 : is an Armstrong Number.
# 407 : is an Armstrong Number.
