# 23.	Write a Python program to show multilevel inheritance. 

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
p.eat()  # Inherited from Animal
p.speak()   # Inherited from Dog 
p.walk() # Own method 


# Output:
# Animal Eats.
# Dog barks.
# Puppy walks.