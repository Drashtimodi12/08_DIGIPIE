# ATM PIN Encapsulation
# Requirements
# Class ATM
# Private:
# __pin
# Methods:
# set_pin() → must be 4 digits
# verify_pin(pin) → return True/False

class ATM:

    def __init__(self):
        self.__pin = 1234

    def get_pin(self):
        return self.__pin
    
    def set_pin(self):
        new_pin = input("Enter new pin: ")

        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = int(new_pin)
            print("Pin changed succesfully...")
        else:
            print("Pin must have 4 digit.")

    def verify_pin(self):
        pin = input("\nEnter pin to verify: ")
        if pin.isdigit() and int(pin) == self.__pin:
            print("Pin is Correct.")
        else:
            print("Invalid Pin.")

a1 = ATM()
a1.set_pin()
a1.verify_pin()
# OP:
# Enter new pin: 9876
# Pin changed succesfully...

# Enter pin to verify: 9876
# Pin is Correct.