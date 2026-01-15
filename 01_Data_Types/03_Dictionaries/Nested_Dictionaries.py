# Nested Dictionaries:- A dictionary can contain dictionaries, this is called nested dictionaries.
student = {
    "std1" : {
        "Name" : "Sejal",
        "Sub" : "Maths"
    }, 
    "std2" : {
        "Name" : "Usha",
        "Sub" : "Gujarati"
    },
    "std3" : {
        "Name" : "Drashti",
        "Sub" : "Hindi"
    }
}
print(student)
# Output:
#  {'std1': {'Name': 'Sejal', 'Sub': 'Maths'}, 'std2': {'Name': 'Usha', 'Sub': 'Gujarati'}, 'std3': {'Name': 'Drashti', 'Sub': 'Hindi'}}

print(student["std1"].keys())       # Output: dict_keys(['Name', 'Sub'])




#  if you want to add three dictionaries into a new dictionary:
std1 = {
    "Name" : "Sejal",
    "Sub" : "Maths"
}
std2 = {
    "Name" : "Drashti",
    "Sub" : "Hindi"
}
std3 = {
    "Name" : "Usha",
    "Sub" : "Gujarati"
}

student = {
    "std1" : std1,
    "std2" : std2,
    "std3" : std3
}

print(student)
# Output:
# {'std1': {'Name': 'Sejal', 'Sub': 'Maths'}, 'std2': {'Name': 'Drashti', 'Sub': 'Hindi'}, 'std3': {'Name': 'Usha', 'Sub': 'Gujarati'}}






# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
student = {
    "std1" : {
        "Name" : "Sejal",
        "Sub" : "Maths"
    }, 
    "std2" : {
        "Name" : "Usha",
        "Sub" : "Gujarati"
    },
    "std3" : {
        "Name" : "Drashti",
        "Sub" : "Hindi"
    }
}
print(student["std2"]["Name"])      # Output: Usha



# Loop Through Nested Dictionaries:- You can loop through a dictionary by using the items() method like this:
student = {
    "std1" : {
        "Name" : "Sejal",
        "Sub" : "Maths"
    }, 
    "std2" : {
        "Name" : "Usha",
        "Sub" : "Gujarati"
    },
    "std3" : {
        "Name" : "Drashti",
        "Sub" : "Hindi"
    }
}
for x, obj in student.items() :
    print(x)

    for y in obj :
        print(y + ":", obj[y])

# Output:
# std1
# Name: Sejal
# Sub: Maths
# std2
# Name: Usha
# Sub: Gujarati
# std3
# Name: Drashti
# Sub: Hindi