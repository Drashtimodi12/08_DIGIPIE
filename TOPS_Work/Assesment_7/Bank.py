import Banker as b
import Customer as c

choice = 0
while choice != 3:
    print("""
    Welcome To Python Bank Management System. \n
    Select Your Role. \n
    1 : Banker
    2 : Customer
    3 : Exit
    """)
    
    try:
        choice = int(input("Choose Your Role: "))
        if choice == 1:
            b.Banker()
        elif choice == 2:
            c.Customer()
        elif choice == 3:
            print("You are EXIT!")
        else:
            print("Invalid Choice...")

    except ValueError:
        print("Invalid Input! Please enter a number.")