# Multilevel Inheritance – Device → Laptop → GamingLaptop
# Requirements:
# Class Device
# method: info()
# Class Laptop(Device)
# method: features()
# Class GamingLaptop(Laptop)
# method: gaming_mode()
# Create object of GamingLaptop and call all three methods.

class Device:
    def info(self):
        self.device = input("Enter Device Name: ")
        print("Your Device Name is: ", self.device)

class Laptop(Device):
    def features(self):
        self.info_laptop = input("Enter Laptop version: ")
        print("Your laptop features is: ", self.info_laptop)


class GamingLaptop(Laptop):
    def gaming_mode(self):
        if self.device.lower() == 'gaming laptop':
            print("Perfect Laptop for gaming.")
        else:
            print("Not perfect for Gamming. please by new laptop.")

g = GamingLaptop()
g.info()
g.features()
g.gaming_mode()
# OP:
# Enter Device Name: iphone
# Your Device Name is:  iphone
# Enter Laptop version: i5
# Your laptop features is:  i5
# Not perfect for Gamming. please by new laptop.