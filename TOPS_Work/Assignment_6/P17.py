# 17.	Write a generator function that generates the first 10 even numbers.
# / Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user. 

# Loop through numbers from 1 to 10
for i in range(1, 11):  
    # Check if the number is even
    if i % 2 == 0:
        print(f'{i} is an even number.')
    else:
        print(f'{i} is an odd number.')

