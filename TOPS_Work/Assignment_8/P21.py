# 21.	Write Python programs to demonstrate different types of inheritance (single, multiple,  multilevel, etc.).

# 1.    Write a Python program to show single inheritance. 

# Parent class
class Animal :
    def speak(self) :
        print("Animal Speaks.")


# Child class inheriting from Animal
class  Dog(Animal) :
    def Bark(self) :
        print("Dog Barks.")

# Creating an object of the Dog class
dog = Dog()
print("****** SINGLE ******")
dog.speak()     # Inherited method from Animal
dog.Bark()      # Own method
print("******************")
# Output:
# Animal Speaks.
# Dog Barks.


# 2.    Write a Python program to show multiple inheritance. 

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
print("****** MULTIPLE ******")
c.height()       # Inherited from Father
c.skin_color()   # Inherited from Mother
c.intelligence() # Own method
print("******************")
# Output:
# Father's height is 6ft.
# Mother has fair skin.
# Child id Intelligent.


# 3.    Write a Python program to show multilevel inheritance. 

# Grandparent class
class Animal:
    def eat(self) :
        print("Animal Eats.")

# Parent class inheriting from Animal
class Dog(Animal):
    def speak(self) :
        print("Dog barks.")

# Child class inheriting from Dog
class puppy(Dog) :
    def walk(self) :
        print("Puppy walks.")

# Creating an object of puppy class
p = puppy()
print("****** MULTLEVEL ******")
p.eat()  # Inherited from Animal
p.speak()   # Inherited from Dog 
p.walk() # Own method 


# Output:
# Animal Eats.
# Dog barks.
# Puppy walks.