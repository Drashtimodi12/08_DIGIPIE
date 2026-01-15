# Login Credentials (Private Only)
# Requirements
# Class Login
# Private:
# __username
# __password
# Setters must validate:
# password length ≥ 6
# must include number
# must include special char (!@#$ etc.)
# check_login() method to verify login.

class Login:

    def __init__(self):
        self.__username = 'admin'
        self.__password = 'admin@123'


    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    

    def set_username(self):
        a = input("Enter username: ")
        self.__username = a

    def set_password(self):
        new_pass = input("Enter password: ")
        
        special_characters = "!@#$%^&*()_+-={}[]|:;'<>,.?/"

        if len(new_pass) < 6:
            print("Password must be at least 6 characters long.")
            return

        if not any(ch.isdigit() for ch in new_pass):
            print("Password must contain at least one number.")
            return

        if not any(ch in special_characters for ch in new_pass):
            print("Password must contain at least one special character (!@#$ etc.).")
            return

        self.__password = new_pass
        print("Password updated successfully!")

    def check_login(self):
        print("\n\nEnter Valid information to login.")
        user = input("\nEnter username: ")
        password = input("Enter Password: ")
        
        if user == self.__username and password == self.__password:
            print("\nLogin Successful. Welcome!")
        else:
            print("\nInvalid username and password.")
        
l1 = Login()
l1.set_username()
l1.set_password()
l1.check_login()
# OP:
# Enter username: admin
# Enter password: admin@123
# Password updated successfully!


# Enter Valid information to login.

# Enter username: admin
# Enter Password: admin@123

# Login Successful. Welcome!