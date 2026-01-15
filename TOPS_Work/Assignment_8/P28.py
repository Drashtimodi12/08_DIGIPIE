# 28.	Write Python programs to demonstrate method overloading and method overriding.


# 1.    Write a Python program to show method overloading. 

class Calculator :
    def add(self, a, b = 0, c = 0) :
        return a + b + c 

# Create an instance of Calculator
calc = Calculator()

# Call the add method with different numbers of arguments
print("****** OVERLODING ******")
print(calc.add(10))       # Output: 10
print(calc.add(10, 20))   # Output: 30
print(calc.add(10, 20, 30))  # Output: 60


# 2.    Write a Python program to show method overriding. 

# Define the superclass
class Animal:
    def speak(self) :
        return "The animals make a sounds."
    
# Define the subclass
class Dog(Animal) :
    # Override the speak method
    def speak(self) :
        return "The Dog barks."
    
# Define another subclass
class Cat(Animal) :
    # Override the speak method
    def speak(self) :
        return "The Cat meows."
    
# Create instances of each class
animal = Animal()
dog = Dog()
cat = Cat()

# Call the overridden methods
print("****** OVERRIDING ******")
print(animal.speak())  # Output: The animals make a sounds.
print(dog.speak())     # Output: The Dog barks.
print(cat.speak())     # Output: The Cat meows.