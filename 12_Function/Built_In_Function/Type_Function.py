a = 10
print(f"{a} data type is {type(a)}")
# OP: 10 data type is <class 'int'>
print("------------------------")

b = 12.5
print(f"{b} data type is {type(b)}")
# OP: 12.5 data type is <class 'float'>
print("------------------------")

c = "Drashti"
print(f"{c} data type is {type(c)}")
# OP: Drashti data type is <class 'str'>
print("------------------------")

d = True
print(f"{d} data type is {type(d)}")
# OP: True data type is <class 'bool'>
print("------------------------")

e = None
print(f"{e} data type is {type(e)}")
# OP: None data type is <class 'NoneType'>
print("------------------------")

f1 = [1, 2, 3]
print(f"{f1} data type is {type(f1)}")
# OP: [1, 2, 3] data type is <class 'list'>
f2 = [2, 5, 2]
print(f"{f2} data type is {type(f2)}")
# OP: [2, 5, 2] data type is <class 'list'>
print("------------------------")

g1 = (4, 5)
print(f"{g1} data type is {type(g1)}")
# OP: (4, 5) data type is <class 'tuple'>
g2 = tuple((2, 4, 2))
print(f"{g2} data type is {type(g2)}")
# OP: (2, 4, 2) data type is <class 'tuple'>
print("------------------------")

h1 = {6, 7}
print(f"{h1} data type is {type(h1)}")
# OP: {6, 7} data type is <class 'set'>
h2 = set((True, 2, 6))
print(f"{h2} data type is {type(h2)}")
# OP: {True, 2, 6} data type is <class 'set'>
print("------------------------")

i1 = {"name": "Modi"}
print(f"{i1} data type is {type(i1)}")
# OP: {'name': 'Modi'} data type is <class 'dict'>
i2 = dict(name = "Modi")
print(f"{i2} data type is {type(i2)}")
# OP: {'name': 'Modi'} data type is <class 'dict'>
print("------------------------")



# Accept input and print datatype
# Take input from user and print:
# value entered
# its datatype

a = input("Enter something: ")
print(f"User input is {a} and there datatype is {type(a)}.")
# OP: 
# Enter something: dras
# User input is dras and there datatype is <class 'str'>.
print("------------------------")



# Find datatype of each key and value

d = {"name": "Drashti", "age": 21, "marks": 88.5}


for k, v in d.items():    
    print(f"Key : {k} -> {type(k).__name__}, Value : {v} -> {type(v).__name__}")
# OP: 
# Key : name -> str, Value : Drashti -> str
# Key : age -> str, Value : 21 -> int
# Key : marks -> str, Value : 88.5 -> float