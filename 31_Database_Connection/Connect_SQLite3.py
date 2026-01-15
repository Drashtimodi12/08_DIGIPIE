import sqlite3  # Importing the SQLite library to interact with the SQLite database

mydb = sqlite3.connect("data.db")   # Connect to (or create) a SQLite database named "data.db"

# Creating a table named 'stu' with columns
# mydb.execute("Create table stu(id int primary key, name varchar(50), email varchar(50))")     


# Inserting a new student record into the 'stu' table
# mydb.execute("insert into stu values(1, 'Drashti', 'd@gmail.com')")
# mydb.commit()         # Saving the changes to the database

# mydb.execute("insert into stu values(2, 'Sejal', 'sejal@gmail.com')")
# mydb.commit()


# Updating the email of the student with id=1
# mydb.execute("update stu set email='drashti@gmail.com' where id=1")
# mydb.commit()


# Selecting all records from the 'stu' table
data = mydb.execute("select * from stu")
# print(data.fetchall())        # Printing all the student records at once

# Printing each student record (tuple) one by one
# for student in data.fetchall():
#     print(student)

# Printing each field of each student record one by one
# for student in data.fetchall():
#     for st in student:
#         print(st)

# Printing each field of each student record in a single line, separated by space
# for student in data.fetchall():
#     for st in student:
#         print(st,end = " ")
#     print()


# Deleting the student record where id=2
# mydb.execute("delete from stu where id = 2")
# mydb.commit()