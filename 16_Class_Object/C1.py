# Task 4: Create a class Book with attributes:
# title
# author
# Add a method display() that prints book details.

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Now a days i read {self.title} book writed by {self.author}")

b1 = Book('Rich Man', 'Drashti')
b2 = Book('Story Book', 'Narendr')

b1.display()
b2.display()
# OP:
# Now a days i read Rich Man book writed by Drashti
# Now a days i read Story Book book writed by Narendr