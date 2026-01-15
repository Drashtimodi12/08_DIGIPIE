# 30.	Write a Python program to show method overriding. 

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
print(animal.speak())  # Output: The animals make a sounds.
print(dog.speak())     # Output: The Dog barks.
print(cat.speak())     # Output: The Cat meows.