# __repr__ → For developers (unambiguous, debugging)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Developer-friendly
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

p = Person("Drashti", 22)

print(repr(p))  # calls __repr__
# p               # also calls __repr__ in Python shell
# OP: Person(name='Drashti', age=22)