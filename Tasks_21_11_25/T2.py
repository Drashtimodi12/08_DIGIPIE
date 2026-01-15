# Write a class Book that takes title and author as parameters 
# in the constructor and prints them when an object is created.

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        print(f"I am Currently reading {self.title} Book.")
        print(f"Author name is {self.author}.")


obj = Book("'The Rich Man'", "Paresh")

# OP:
# I am Currently reading 'The Rich Man' Book.
# Author name is Paresh.