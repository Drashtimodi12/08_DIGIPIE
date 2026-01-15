# Function that takes a string and returns the number of vowels in it.

def vowels():
    a = input("Enter Sentence: ").lower()
    count = 0
    for i in a:
        if i in 'aeiou':
            count+=1
    return count
print(f"In this Sentence {vowels()} vowels.")
# OP:
# Enter Sentence: My name is drashti
# In this Sentence 5 vowels.