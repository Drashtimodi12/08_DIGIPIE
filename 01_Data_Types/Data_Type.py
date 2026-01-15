# Python Datatypes

# Text Type:	str
name = "Drashti"    # A string variable
print(type(name))  # Output: <class 'str'>



# Numeric Types:	int, float, complex
a = 10          # Integer type
print(type(a))  # Output: <class 'int'>

b = 25.34       # Float type
print(type(b))  # Output: <class 'float'>

c = 4+5j        # Complex number
print(type(c))  # Output: <class 'complex'>
print(c.real)   # Real part of the complex number, Output: 4.0
print(c.imag)   # Imaginary part of the complex number, Output: 5.0
print(c.conjugate())  # Conjugate of the complex number, Output: (4-5j)



# Sequence Types:	list, tuple, range
l = [20, 30, 10, 40, 10]    # List (mutable)
print(l)  # Output: [20, 30, 10, 40, 10]

t = (10, 30, 80, 20, 10)    # Tuple (immutable)
print(t)  # Output: (10, 30, 80, 20, 10)

r = range(1, 10, 2)  # Range from 1 to 9 with a step of 2
print(list(r))  # Output: [1, 3, 5, 7, 9]



# Mapping Type:	dict
d = {"10":"Python","20":"Java"}  # Dictionary stores key-value pairs
print(d)  # Output: {'10': 'Python', '20': 'Java'}



# Set Types:	set, frozenset
s = {10, 20, 40, 10, 70, 50}    # Set (unordered, unique values)
print(s)  # Output: {50, 20, 70, 40, 10}

f = frozenset({10,20,30,40})    # Immutable set
print(f)  # Output: frozenset({10, 20, 30, 40})



# Boolean Type:	bool
b = True    # Boolean (True or False)
print(b)  # Output: True



# Binary Types:	bytes, bytearray, memoryview
binary_data = bytes([65, 66, 67])  # Bytes type (immutable)
print(binary_data)  # Output: b'ABC'

mutable_binary = bytearray([65, 66, 67])  # Bytearray (mutable)
print(mutable_binary)  # Output: bytearray(b'ABC')

memory_view = memoryview(bytes([65, 66, 67]))  # Memoryview type
print(memory_view)  # Output: <memory at ...>



# None Type:	NoneType
k = None        # Represents 'no value' or 'null'
print(type(k))  # Output: <class 'NoneType'>