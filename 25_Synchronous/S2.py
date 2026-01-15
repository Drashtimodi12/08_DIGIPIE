# Synchronous Execution:
# Call all the functions one by one in the program and print the results step by step.

import time

def fun1():
    time.sleep(3)
    print("Function 1 printing time 3 second")

def fun2():
    time.sleep(5)
    print("Function 2 printing time 5 second")

def fun3():
    time.sleep(10)
    print("Function 3 printing time 10 second")


def main():
    fun1()
    fun2()
    fun3()

main()

# OP:
# Function 1 printing time 3 second
# Function 2 printing time 5 second
# Function 3 printing time 10 second



