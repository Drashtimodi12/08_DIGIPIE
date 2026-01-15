def demo():
    try:
        a = int(input("Enter integer number: "))
        print("You enter: ", a)
    except Exception as e:
        print(e)
    finally:
        print("Finally Block Executed. ")

d = demo()
# OP:
# Enter integer number: -2
# You enter:  -2
# Finally Block Executed.