# __add__(self, other): This dunder method lets you define
# how the + operator should behave for objects of a class.

class Number:
    # Constructor to store a number value
    def __init__(self, value):
        self.value = value

    # Overloading the + operator
    # n1 + n2 internally calls n1.__add__(n2)
    def __add__(self, other):
        return self.value + other.value   # Adding values inside both objects

# Creating two objects
n1 = Number(5)
n2 = Number(10)

# When we use + between objects, __add__ method gets triggered
print(n1 + n2)
# OP: 15