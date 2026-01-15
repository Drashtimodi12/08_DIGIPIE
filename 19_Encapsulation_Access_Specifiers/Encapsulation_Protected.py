class A:
    def __init__(self):
        self._salary = 3000     # Protected attribute (convention: should not be accessed outside class)

a = A()                         # Create object
print(a._salary)                # Can access, but NOT recommended
# OP:
3000