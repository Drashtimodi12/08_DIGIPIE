# Take a list of numbers from the user (or predefined) and calculate:
# Sum of elements
# Average value

l = [1, 5, 8, 2]
sum =0 
for i in l:
    sum += i

ave = sum/len(l)

print("Sum =", sum)         # OP:   Sum = 16
print("Average =", ave)     # OP:   Average = 4.0