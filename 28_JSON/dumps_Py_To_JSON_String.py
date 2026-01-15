"""
json.dumps()
    dumps = “dump to string”
    It converts Python object → JSON string

When do we use json.dumps()?
    Sending data through API
    Storing JSON in a file
    Logging/outputting JSON
    Converting Python objects for network transfer

    Parameter	            Meaning
    indent	            pretty formatting
    sort_keys	        sorts keys alphabetically
    ensure_ascii=False	allows Hindi, Gujarati, emojis, non-English text
    skipkeys=True	    ignores invalid keys
    default	handle      custom objects
"""

import json

data = {
    "name": "Drashti",                  # String
    "age": 22,                          # Integer
    "percentage": 89.75,                # Float
    "is_student": True,                 # Boolean
    "married": False,                   # Boolean
    "hobbies": ["coding", "music"],     # List
    "marks": (90, 85, 88),              # Tuple → converted to array
    "address": {                        # Nested dictionary
        "city": "Surat",
        "state": "Gujarat"
    },
    "nothing": None                     # None → null
}
print("Before conversion, Data format is ", type(data))    

print("\n=============================\n")
json_str = json.dumps(data, indent=4, sort_keys=True) 
print(json_str)         
print("After conversion, Data format is ", type(json_str))



# OP: 
# Before conversion, Data format is  <class 'dict'>

# =============================

# {
#     "address": {
#         "city": "Surat",
#         "state": "Gujarat"
#     },
#     "age": 22,
#     "hobbies": [
#         "coding",
#         "music"
#     ],
#     "is_student": true,
#     "marks": [
#         90,
#         85,
#         88
#     ],
#     "married": false,
#     "name": "Drashti",
#     "nothing": null,
#     "percentage": 89.75
# }
# After conversion, Data format is  <class 'str'>