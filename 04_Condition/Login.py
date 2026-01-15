# Ask user input and check:
# If both correct → Login successful
# If username wrong → Invalid username
# If password wrong → Wrong password

username = "admin"
password = "python123"

user_input = input("Enter username: ")
pass_input = input("Enter passweord: ")

if username == user_input and password == pass_input:
    print("Login successful! Welcome to Python world.")
elif username != user_input and password != pass_input:
    print("Username and Password both are wrong.")
elif username != user_input:
    print("Invalid username.")
else:
    print("Wrong password.")

# OP:
# Enter username: admin
# Enter passweord: python123
# Login successful! Welcome to Python world.