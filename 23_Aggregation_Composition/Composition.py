"""
Composition:- Composition is a strong “HAS–A” relationship between two classes where one class owns another class.
The child object cannot exist without the parent object.

Parent creates the object of another class inside it.
Child object’s lifetime depends on the parent.

Example:
A Human has a Heart
If the human dies → the heart also stops existing
Heart cannot live independently

So instead of inheriting, we use objects inside another class.
"""

class Heart:
    def beat(self):
        print("Heart is beating...")

class Human:
    def __init__(self):
        # Creating Heart object inside Human
        # Heart cannot exist without Human → Composition
        self.heart = Heart()        # Calling parent class

    def live(self):
        print("Human is living...")
        self.heart.beat()       # Calling parent class method

h = Human()
h.live()
# OP:
# Human is living...
# Heart is beating...

"""
✔ Key Checks:
Child object created inside parent → yes (self.heart = Heart())
Strong HAS-A → correct
Dependent lifetime → correct
Human cannot work without Heart → correct

Comments clearly explain:
✔ Heart created inside Human
✔ Heart cannot exist without Human
✔ Strong relationship
"""
