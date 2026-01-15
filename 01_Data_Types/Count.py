data = [10, 2, "abc", 4.5, True, [1,2], {"a":1}, (3,4)]


item_count = {}

for i in data:
    t = type(i).__name__
    
    if t in item_count:
        item_count[t] += 1
    else:
        item_count[t] = 1

for k, v in item_count.items():
    print(f"{k}: {v}")    


# OP:
# int: 2
# str: 1  
# float: 1
# bool: 1 
# list: 1 
# dict: 1 
# tuple: 1