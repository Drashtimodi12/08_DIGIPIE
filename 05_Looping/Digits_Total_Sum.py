# Input a number and calculate:
# Total digits
# Sum of digits using a loop

num = input("Enter digits: ")
total_digigts = 0
sum_num = 0

for i in num:
    total_digigts += 1
    sum_num += int(i)
    
print("Total number: ", total_digigts)
print("Sum of Digits: ", sum_num)
# OP:
# Enter digits: 12
# Total number:  2
# Sum of Digits:  3

print("\n========================\n")

num1 = int(input("Enter digits: "))
total_digit = 0
sum_num = 0
temp = num1
while temp > 0:
    digit = temp % 10          # get last digit
    sum_num += digit            # add to sum
    total_digit += 1           # increment count
    temp = temp // 10           # remove last digit
    
print("Total number: ", total_digit)
print("Sum of Digits: ", sum_num)
# OP:
# Enter digits: 5
# Total number:  1
# Sum of Digits:  5