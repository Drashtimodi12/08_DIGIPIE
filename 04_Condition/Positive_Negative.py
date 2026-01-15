# Number is Positive, Negative, or Smallest/Largest Range
# check if it lies between 10 and 50

a = float(input("Enter a number: "))

if a >= 0:
    print(f"{a} is positive.")
    if 10 <= a <= 50:
        print(f"{a} is lies between 10 to 50.")
    else:
        print(f"{a} is not lies between 10 to 50.")
else:
    print(f"{a} is negative.")
# OP:
# Enter a number: -12
# -12.0 is negative.