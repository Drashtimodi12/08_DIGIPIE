# 40.	Write a Python program to generate random numbers using the random module.

# Import the random module
import random

# Generate a random integer between 1 and 1000
random_int = random.randint(1, 1000)
print("Random INTEGER between 1 to 1000 is: ", random_int)
# Output: Random INTEGER between 1 to 1000 is:  456

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print("Random floating-point number between 0 and 1: ", random_float)
# Output: Random floating-point number between 0 and 1:  0.6440436783678234

# Generate a random floating-point number between a specified range, e.g., 1.5 and 5.5
random_uniform = random.uniform(1, 10)
print("Random floating-point number between 1 and 10: ", random_uniform)
# Output: Random floating-point number between 1 and 10:  2.0887210916140235

# Generate a random number from a normal distribution with mean 0 and standard deviation 1
random_normal = random.gauss(0, 1)
print("Random number from a normal distribution (mean=0, std=1): ", random_normal)
# Output: Random number from a normal distribution (mean=0, std=1):  -0.34120004307181945