# Define a dictionary to store customer data
customers = {
    "1001": {"Name": "Sejal", "Balance": 5000.0},
    "1002": {"Name": "Drashti", "Balance": 3000.0},
    "1003": {"Name": "Usha", "Balance": 7000.0},
}

def Customer():
    while True:
        print("""
        Welcome To Customer's Portal. \n
        Operation Menu \n  
        1 : Withdraw Amount  
        2 : Deposit Amount  
        3 : View Balance  
        4 : Exit to Main Menu  
        """)
        
        try:
            op = int(input("Enter operation number: "))
            A_No = input("Enter Your Account Number: ")

            if A_No not in customers:
                print("Account does not exist!")
                continue

            if op == 1:  # Withdraw Amount
                amount = float(input("Enter Amount to Withdraw: "))
                if amount > customers[A_No]["Balance"]:
                    print("Insufficient Balance!")
                else:
                    customers[A_No]["Balance"] -= amount
                    print(f"₹{amount} Withdrawn Successfully!")

            elif op == 2:  # Deposit Amount
                amount = float(input("Enter Amount to Deposit: "))
                customers[A_No]["Balance"] += amount
                print(f"₹{amount} Deposited Successfully!")

            elif op == 3:  # View Balance
                print(f"Your Balance: ₹{customers[A_No]['Balance']}")

            elif op == 4:  # Exit Customer Menu
                print("Returning to Main Menu...\n")
                break

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")