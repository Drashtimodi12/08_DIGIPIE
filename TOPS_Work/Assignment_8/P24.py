# 24.	Write a Python program to show multiple inheritance. 

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