"""
json.loads()
    loads = “load from string”
    It converts JSON string → Python object

When do we use json.loads()?
    Reading API response
    Reading JSON from database
    Parsing JSON strings
    Converting JSON input to Python for processing

Parameter	        Meaning
object_hook	    modify dictionary after loading
parse_int	    custom function to parse integers
parse_float	    custom function for floats
strict=False	allows trailing commas      
"""

# Convert JSON → Python

import json

# Use json.loads() ONLY when the input is a string
json_str = """
{
    "name": "Drashti",
    "age": 22,
    "percentage": 89.75,
    "is_student": true,
    "married": false,
    "hobbies": ["coding", "music"],
    "marks": [90, 85, 88],
    "address": {
        "city": "Surat",
        "state": "Gujarat"
    },
    "nothing": null
}
"""

print("Before conversion, Data format is ", type(json_str))    # OP: JSON data is  <class 'str'>
data = json.loads(json_str) 

print("\n=============================\n")
# Converts JSON string → Python object (dict)
print("After conversion, Data format is ", type(data))
print(data)         

# op:
# Before conversion, Data format is  <class 'str'>

# =============================

# After conversion, Data format is  <class 'dict'>
# {'name': 'Drashti', 'age': 22, 'percentage': 89.75, 'is_student': True, 'married': False, 'hobbies': ['coding', 'music'], 'marks': [90, 85, 88], 'address': {'city': 'Surat', 'state': 'Gujarat'}, 'nothing': None}