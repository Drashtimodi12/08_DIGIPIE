# Continue with String
# Iterate through a string "Python" and skip vowels using continue.
# Print only consonants.

a = "Python"
vowel ='aeiouAEIOU'

for i in a:
    if i in vowel:
        continue
    else:
        print(i, end = " ")
# OP: P y t h n 