from multipledispatch import dispatch

class Calc:
    # Overloaded method with two integer parameters
    @dispatch(int, int)
    def add(self, a, b):
        result = a + b
        print("Result of adding two integers:", result)

    # Overloaded method with three integer parameters
    @dispatch(int, int, int)
    def add(self, a, b, c):
        result = a + b + c
        print("Result of adding three integers:", result)

    # Overloaded method with an integer and a float parameter
    @dispatch(int, float)
    def add(self, a, b):
        result = a + b
        print("Result of adding an integer and a float:", result)

# Create an instance of Calc
c = Calc()
# Call the overloaded add methods
c.add(10, 20)
c.add(10, 20, 30)
c.add(30, 45.0)


# output:
# Result of adding two integers: 30
# Result of adding three integers: 60
# Result of adding an integer and a float: 75.0