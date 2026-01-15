# 11.	Write a Python program to calculate grades based on percentage using if-else ladder.

# Taking student marks as input
marks = float(input('Enter Student Marks (0-100): '))  

# Check if marks are in the valid range
if marks < 0 or marks > 100:
    print('Invalid Input: Please enter marks between 0 and 100.')  # Error message for invalid marks
elif marks >= 90:  
    print('A Grade')  # If marks are 90 or above, print A Grade
elif marks >= 70:  
    print('B Grade')  # If marks are between 70 and 89, print B Grade
elif marks >= 50:  
    print('C Grade')  # If marks are between 50 and 69, print C Grade
elif marks >= 35:  
    print('D Grade')  # If marks are between 35 and 49, print D Grade
else:  
    print('E Grade')  # If marks are between 0 and 34, print E Grade
