# 10.	Write a Python program to check if a number is prime using if_else.

# Prime number : number which is divisible by itself is called prime number.

# Taking input from the user
num = int(input('Enter a number: '))
flag = 0

# Loop through numbers from 2 to number-1 (because 1 and number itself are not checked)
for i in range(2, num):  
    if num % i == 0:  # If number is divisible by any i, it's not prime
        flag = 1  # Set flag to 1 indicating it's not prime
        break  # Exit the loop as we found a divisor

# After the loop, check the flag value
if flag == 0:  
    print(f'The number {num} is prime.')     # If flag is still 0, the number is prime
else:  
     print(f'The number {num} is not prime.')  # If flag is 1, the number is not prime