"""
json.dump()
    dump = write JSON to a file
    json.dump() is used to write Python data → into a JSON file direcrtly.

When do we use json.dump()?
    Save Python data to a JSON file
    Configuration files
    Exporting data
    Writing logs in JSON format

        Parameter	                 Use
    indent	                    pretty output
    sort_keys	                alphabetical sorting
    ensure_ascii=False	        supports non-English text
    separators=(", ", " : ")	custom separators
    Same parameters as dumps()	because they behave similarly
"""

# Write dictionary to a JSON file

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

with open('dump_Py_To_JSON_File.json', 'w') as file:
    json.dump(data, file, indent=4)