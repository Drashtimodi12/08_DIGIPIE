# Create a class Fruit with attributes name and taste. 
# Use the str method to return a formatted string like "Apple tastes sweet".

class Fruit:

    def __init__(self, name, taste):
        self.name = name
        self.taste = taste

    def __str__(self):
        return f"{self.name} tastes {self.taste}."
    
f1 = Fruit('Apple', 'sweet')

print(f1)
# OP: Apple tastes sweet.