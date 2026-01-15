student = {"name": "Drashti", "age": 21, "city": "Surat"}

# Print keys
print(student.keys())       # dict_keys(['name', 'age', 'city'])
print("------------------------")

# Print values
print(student.values())     # dict_values(['Drashti', 21, 'Surat'])
print("------------------------")

# Change city → Ahmedabad
student.update(city='Ahmedabad')        # dict_items([('name', 'Drashti'), ('age', 21), ('city', 'Ahmedabad')])
print(student.items())
print("------------------------")

# Add new key: "degree": "B.Tech"
student.update(degree = 'B.Tech')
print(student.items())              # dict_items([('name', 'Drashti'), ('age', 21), ('city', 'Ahmedabad'), ('degree', 'B.Tech')])
print("------------------------")

# Remove "age"
student.pop('age')
print(student.items())          # dict_items([('name', 'Drashti'), ('city', 'Ahmedabad'), ('degree', 'B.Tech')])

