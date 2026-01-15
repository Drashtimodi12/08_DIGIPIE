# 31.	Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data.

import sqlite3

mydb = sqlite3.connect("example.db")    # Connect to SQLite3 database (it creates the file if it doesn't exist)

cursor = mydb.cursor()  # Create a cursor object

# cursor.execute("create table users(id integer primary key autoincrement , name varchar(20) not null, email varchar(50) not null)")
# Create table (use INTEGER PRIMARY KEY AUTOINCREMENT for auto-incrementing id)

# Insert data into the table (use ? placeholders to avoid SQL injection)
# cursor.execute("insert into users (name, email) values ('Drashti', 'd@example.com')")
# cursor.execute("insert into users (name, email) values ('Sejal', 's@gmail.com')")
# cursor.execute("insert into users (name,email) values ('rudra','R@gmail.com')")
               
mydb.commit()   # Save changes

cursor.execute("select * from users")   # Fetch and print data
rows = cursor.fetchall()

print("User Table Data:")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

mydb.close()    # Close the connection