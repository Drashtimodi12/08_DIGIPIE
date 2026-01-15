def Banker():
    # Dictionary to store customer data
    customers = {}
    choice = "Y"
    
    # Loop until the user chooses to exit
    while choice != "N":
        print("""
        Welcome To Banker's App. \n
        Operation Menu. \n
        1 : Add Customer
        2 : View All Customers
        3 : Search Customer
        4 : Total Amount in Bank
        5 : Exit Banker Menu
        """)

        try:
            # Get user's choice of operation
            op = int(input("Enter operation which you want to perform: "))

            if op == 1:  # Add Customer
                A_No = int(input("Enter Account Number: "))
                if A_No in customers:
                    print("Account already exists!")
                else:
                    Name = input("Enter Your Name: ")
                    Balance = float(input("Enter Opening Balance: "))
                    customers[A_No] = {"Name": Name, "Balance": Balance}  # Corrected the update method
                    print("Customer added successfully!")
                    print(customers)

            elif op == 2:  # View All Customers
                print("Customer List \n")
                for acc, details in customers.items():
                    print(f"Account No: {acc}, Name: {details['Name']}, Balance: ₹{details['Balance']}")

            elif op == 3:  # Search Customer
                A_No = int(input("Enter Account Number to search: "))
                if A_No in customers:
                    print(f"Customer Found: {customers[A_No]}")
                else:
                    print("Customer not found!")

            elif op == 4:  # View Total Bank Balance
                total = sum(customer["Balance"] for customer in customers.values())
                print(f"Total Amount in Bank: ₹{total}")

            elif op == 5:  # Exit Banker Menu
                print("Returning to Main Menu...\n")
                break

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")
        
        choice = input("Do you want to perform more operations? (Y or N): ").upper()