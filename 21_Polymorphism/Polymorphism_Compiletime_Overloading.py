"""
Compile-time Polymorphism (Method Overloading):-  Same function name, different parameters.
    In method overloading, inheritance is NOT required.
    Python does NOT support real method overloading because Python is an interpreted language, which means:
    Only the last method with the same name is kept.
But we can achieve overloading-like behavior using:
    *args
    **kwargs
    default parameters
"""


# Incorrect (Python does not support real overloading)-->  Only the last myfun() survives.
# class overloading:

#     def myfun(self):
#         print('Function with no argument.')

#     def myfun(self, a):
#         print('Function with 1 argument.')

#     def myfun(self, b, c):
#         print('Function with 2 argument.')

# ol = overloading()

# ol.myfun(10)    # ERROR
# ol.myfun(10, 20)





# Overloading using *args (Correct)
class Overloading:

    def myfun(self, *args):
        if len(args) == 0:
            print("Function with no argument.")
        elif len(args) == 1:
            print("Function with 1 argument.")
        elif len(args) == 2:
            print("Function with 2 arguments.")
        else:
            print("Function with many arguments.")

ol = Overloading()
ol.myfun()
ol.myfun(10)
ol.myfun(10, 20)
ol.myfun(1, 2, 3, 4)
# OP:
# Function with no argument.
# Function with 1 argument.
# Function with 2 arguments.
# Function with many arguments.