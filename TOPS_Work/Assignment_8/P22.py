# 22.	Write a Python program to show single inheritance. 

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
dog.speak()     # Inherited method from Animal
dog.Bark()      # Own method

# Output:
# Animal Speaks.
# Dog Barks.