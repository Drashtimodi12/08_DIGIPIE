# Create a base class Bird with a method fly(). Create two subclasses Sparrow and Penguin that 
# override fly() differently. Write a function that takes any Bird object and calls its fly() method.

class Bird:
    def fly(self):
        print("Most birds can fly.")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying in the sky.")

class Penguin(Bird):
    def fly(self):
        print("Penguin is bird, but it cann't fly in the sky.")


def bird_fly(bird):
    bird.fly()


b = Bird()
bird_fly(b)  

s = Sparrow()
bird_fly(s)  

p = Penguin()
bird_fly(p)

# OP:
# Most birds can fly.
# Sparrow flying in the sky.
# Penguin is bird, but it cann't fly in the sky.