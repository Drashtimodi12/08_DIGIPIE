# __len__(self): This dunder method allows a class to define
# what value should be returned when len(object) is used.
# __len__ should normally return the size of something (list, items, entries, etc.).
# Now the class behaves like a container whose length is the number of elements in the list.

class length:

    # Constructor - stores a list or any collection
    def __init__(self, num):
        self.number = num  # Here 'num' is a list: [1, 4, 6]

    # __len__ returns the length of the stored list.
    # Whenever len(object) is called, Python runs this method.
    def __len__(self):
        return len(self.number)   # Return actual list length

# Creating an object with a list
l = length([1, 4, 6])

# len(l) internally calls l.__len__()
print(len(l))
# OP: 3