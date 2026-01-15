# User-defined Function:
# Create a function square_list(numbers) that returns a new list with the square of each number.


def square_list(numbers):
    new_list = []
    for i in numbers:
        new_list.append(i*i)
    return new_list

    
a = [1, 2, 3, 4, 5]
print(f"Square of list all number is: {square_list(a)}")

# OP: Square of list all number is: [1, 4, 9, 16, 25]
