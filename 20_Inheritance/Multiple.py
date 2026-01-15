"""
Multiple Inheritance  
One child → inherits from two or more parents  
Example: Mother → Son ← Father  
Child gets features of both parents
"""

# First parent class
class Mother:
    # Method of Mother class
    def cooking(self):
        print("Mother cooks all days..")

# Second parent class
class Father:
    # Method of Father class
    def driving(self):
        print("Father drives car..")

# Child class inheriting from BOTH Mother and Father
class Son(Mother, Father):
    # Child's own method
    def study(self):
        print("Child studies")

# Creating object of Child class
s = Son()

# Calling Mother's method using Son object
s.cooking()

# Calling Father's method using Son object
s.driving()

# Calling Son's own method
s.study()
# OP:
# Mother cooks all days..
# Father drives car..
# Child studies





print("\n==================================\n")





# A child class inherits from multiple parent classes.

# Parent class 1
class Father :
    def height(self) :
        print("Father's height is 6ft.")

# Parent class 2
class Mother :
    def skin_color(self) :
        print("Mother has fair skin.")

# Child class inheriting from both Father and Mother
class Child(Father, Mother) :
    def intelligence(self) :
        print("Child id Intelligent.")

# Creating an object of the Child class
c = Child()
c.height()       # Inherited from Father
c.skin_color()   # Inherited from Mother
c.intelligence() # Own method

# Output:
# Father's height is 6ft.
# Mother has fair skin.
# Child id Intelligent.