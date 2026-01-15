"""
Runtime Polymorphism (Method Overriding)
    Same function name with same arguments in parent and child class.
    Inheritance is compulsory.
    Child class method overrides the parent class method at runtime.
    Python always calls the most derived (child) class method first.
"""

# class Animal:
#     def sound(self):
#         print("Animals make sound.")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks.")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows.")

# # Object of each class
# a = Animal()
# d = Dog()
# c = Cat()

# a.sound()
# d.sound()
# c.sound()





# Parent class
class cl1:
    def myfun(self, a):
        # This method will be overridden in child classes
        print("Class cl1 function called.")
    
# Child class inheriting from cl1
class cl2(cl1):
    def myfun(self, a):
        # This overrides cl1's myfun()
        print("Class cl2 function called.")
        # Calling parent class method using super()
        super().myfun(10)

# Child of cl2 (multi-level inheritance)
class cl3(cl2):
    def myfun(self, a):
        # This overrides cl2's myfun()
        print("Class cl3 function called.")
        # Calling cl2 method using super()
        super().myfun(20)

# Creating object of cl3 (most derived class)
c = cl3()

# Calls cl3's myfun() first → then cl2 → then cl1
c.myfun(30)
# OP:
# Class cl3 function called.
# Class cl2 function called.
# Class cl1 function called.