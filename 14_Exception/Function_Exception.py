# Function definition
def test() :
    try :
        # Taking user input and converting it to an integer
        a = int(input("Enter Number: "))
        return 1        # If the input is valid (no exception occurs), return 1
    except Exception as e :
        return 0        # If an exception occurs (e.g., input is not an integer), return 0
    finally :
        # This block always executes, regardless of whether an exception occurs or not
        print("Printing in the function...")  

k = test()      # Calling the function and storing the return value in variable k
print(k)        # Printing the returned value


# 1 Output:
# Enter Number: 10
# Printing in the function...
# 1

# 2 Output:
# Enter Number: 23.01
# Printing in the function...
# 0