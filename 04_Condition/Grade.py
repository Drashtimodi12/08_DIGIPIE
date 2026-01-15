# Take input for student marks and convert it to an integer
marks = int(input("Student Marks: "))  

# Check the grade based on the marks
if marks >= 90:  
    print("A Grade")  # If marks are 90 or above, print A Grade
elif marks >= 70:  
    print("B Grade")  # If marks are between 70 and 89, print B Grade
elif marks >= 50:  
    print("C Grade")  # If marks are between 50 and 69, print C Grade
elif marks >= 35:  
    print("D Grade")  # If marks are between 35 and 49, print D Grade
elif marks >= 0:  
    print("E Grade")  # If marks are between 0 and 34, print E Grade
else:  
    print("Invalid Input: Enter Marks Between 0 to 100")  # If marks are negative, print an error message


# OP:
# Student Marks: 75
# B Grade