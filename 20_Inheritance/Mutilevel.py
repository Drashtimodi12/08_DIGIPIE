"""
Multilevel Inheritance  
Inheritance chain (Grandparent → Parent → Child)  
Example: A → B → C  
Each child inherits from the class above it
"""


# Level 1: Grandfather class (base class)
class Grandfather:
    # Method of Grandfather
    def property(self):
        print("Grandfather has land.")

# Level 2: Father inherits Grandfather
class Father(Grandfather):
    # Method of Father
    def car(self):
        print("Father has land and car.")

# Level 3: Son inherits Father
class Son(Father):
    # Method of Son
    def govement_job(self):
        print("Son has land, car, and government job.")



# Creating object of Son class (last level)
c = Son()

# Son can access Grandfather's property() because of multilevel inheritance
c.property()

# Son can access Father's car() method
c.car()

# Son's own method
c.govement_job()
# OP:
# Grandfather has land.
# Father has land and car.
# Son has land, car, and government job.



print("/n==================================/n")





# A child class inherits from another child class, forming a chain.

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