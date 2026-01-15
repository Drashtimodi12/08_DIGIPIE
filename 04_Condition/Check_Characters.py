# Check if Character is Vowel, Consonant, Digit, or Special Symbol
# Input a single character and check:
# vowel (a,e,i,o,u)
# consonant
# digit
# special character
# (Use membership operators in/not in)

a = input("Enter a single character:")
vowel = 'aeiouAEIOU'

if a.isalpha():
    if a in vowel:
        print(f"{a} is vowel.")
    else:
        print(f"{a} is constant")
elif a.isdigit():
    print(f"{a} is digits.")
else:
    print(f"{a} is special character.")

# OP:
# Enter a single character:s
# s is constant