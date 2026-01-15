d = {'std1' : {
        'id' : 1,
        'name' : 'drashti',
        'marks' : 45
    },
    'std2' : {
        'id' : 2,
        'name' : 'daizy',
        'marks' : 48
    },
    'std3' : {
        'id' : 1,
        'name' : 'sejal',
        'marks' : 34
    },
    'std4' : {
        'id' : 1,
        'name' : 'zeel',
        'marks' : 46
    },
    'std5' : {
        'id' : 1,
        'name' : 'ansh',
        'marks' : 43
    }
}

# print all names
for student in d.values():
    print(student['name'])
# drashti
# daizy
# sejal
# zeel
# ansh
print("------------------------")

# find highest marks
large = max(d.values(), key=lambda x : x ['marks'])
print(large['name'], large['marks'])       # daizy 48
