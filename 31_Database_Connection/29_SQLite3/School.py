import sqlite3
import os

print("\n=== SCHOOL DATABASE ===\n")

# -----------------------------------
# Task 1: Create Database & Table
# -----------------------------------
con = sqlite3.connect('School.db')      # Connect to database (creates file if not exists)
cur = con.cursor()          # Create a cursor object. It helps to execute SQL queries in the database

cur.execute('''
    CREATE TABLE IF NOT EXISTS Student (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        AGE INTEGER NOT NULL,
        MARKS REAL NOT NULL
    )
''')
con.commit()

print("Table created successfully.")

print("\n-------------------------------\n")

# -----------------------------------
# Task 2: Insert Data
# -----------------------------------
print("Inserting student records...\n")

# #   Single insert
# cur.execute('INSERT INTO Student (NAME, AGE, MARKS) VALUES ("John Doe", 20, 85.5)')
# con.commit()

# #   Multiple inserts (executemany)
# cur.execute("""
#         INSERT INTO Student (NAME, AGE, MARKS) VALUES
#         ("ROZE", 22, 90.0), 
#         ("MIKE", 21, 88.5), 
#         ("ANNA", 23, 92.0),
#         ("LUCY", 20, 87.0), 
#         ("JAMES", 22, 89.5), 
#         ("SOPHIA", 21, 91.0),
#         ("DAVID", 23, 86.0)
#         """)
# con.commit()

print("complete: Students inserted.")

print("\n-------------------------------\n")

# -----------------------------------
# Task 3: SELECT Queries
# -----------------------------------
print("Displaying all students...")
students = cur.execute("SELECT * FROM Student")
print(students.fetchall(), "\n")
con.commit()

# Select students with: Age > 21
print("Students with AGE greater than 21...")
stu_age_greater_21 = cur.execute("SELECT * FROM Student WHERE AGE > 21")
print(stu_age_greater_21.fetchall(), "\n")
con.commit()

# Select students with: Marks > 90
print("Students with MARKS greater than 90...")
Stu_marks_greater_90 = cur.execute("SELECT * FROM Student WHERE MARKS > 90")
print(Stu_marks_greater_90.fetchall(), "\n")
con.commit()

# Select students with: Name starting with “A” (use LIKE)
print("Students with NAME starting with 'A'...")
stu_name_starts_A = cur.execute("SELECT * FROM Student WHERE NAME LIKE 'A%'")
print(stu_name_starts_A.fetchall(), "\n")
con.commit()

# Select students with: Select specific columns (Name, Marks)
print("Fetching NAME and MARKS of all students...")
stu_name_marks = cur.execute("SELECT NAME, MARKS FROM Student")
print(stu_name_marks.fetchall(), "\n")
con.commit()

print("\n-------------------------------\n")

# -----------------------------------
# Task 4: UPDATE Queries
# -----------------------------------
print("Updating MARKS of ID=1...")
cur.execute("UPDATE Student SET MARKS = 95 WHERE ID = 1")
Stu_updated_data = cur.execute("SELECT * FROM Student WHERE ID = 1")
print(Stu_updated_data.fetchall(), "\n")
con.commit()
print("Updated successfully.\n")

# Give 5 extra marks to all students with marks < 85.
print("Giving 5 extra MARKS to students with MARKS less than 85...")
cur.execute("UPDATE Student SET MARKS = MARKS + 5 WHERE MARKS < 85")
stu_updated_data_extra = cur.execute("SELECT * FROM Student WHERE MARKS < 90")
print(stu_updated_data_extra.fetchall(), "\n")
con.commit()

print("\n-------------------------------\n")

# -----------------------------------
# Task 5: DELETE Queries
# -----------------------------------
print("Deleting student where ID = 8...")
cur.execute("DELETE FROM Student WHERE ID = 8")
con.commit()
print("Deleted record with ID = 8 (if existed).\n")

# Delete all students with marks < 86.
print("Deleting student records with MARKS less than 86 ...")
cur.execute("DELETE FROM Student WHERE MARKS < 86")
stu_after_marks_delete = cur.execute("SELECT * FROM Student")
print(stu_after_marks_delete.fetchall(), "\n")
con.commit()

print("\n-------------------------------\n")

# -----------------------------------
# Task 6: ORDER BY & LIMIT
# -----------------------------------
# Select students ordered by marks (descending).
print("Students ordered by MARKS (descending)...")
stu_max_marks_top3 = cur.execute("SELECT * FROM Student ORDER BY MARKS DESC LIMIT 3")
print(stu_max_marks_top3.fetchall(), "\n")
con.commit()

# Select top 3 students with highest marks.
print("Top 3 students with highest MARKS...")
stu_marks_top_3 = cur.execute("SELECT * FROM Student ORDER BY MARKS DESC LIMIT 3")
print(stu_marks_top_3.fetchall(), "\n")
con.commit()

print("\n-------------------------------\n")

# -----------------------------------
# Task 7: Aggregate Functions
# -----------------------------------
#  Maximum marks
print("Maximum MARKS of all students...")
stu_max_marks = cur.execute("SELECT * FROM STUDENT WHERE MARKS = (SELECT MAX(MARKS) FROM Student)")
print(stu_max_marks.fetchall(), "\n")
con.commit()

#  Minimum marks
print("Minimum MARKS of all students...")
stu_min_marks = cur.execute("SELECT * FROM Student WHERE MARKS = (SELECT MIN(MARKS) FROM Student)")
print(stu_min_marks.fetchall(), "\n")
con.commit()

#  Average marks
print("Average MARKS of all students...")
stu_avg_marks = cur.execute("SELECT AVG(MARKS) FROM Student")
print(stu_avg_marks.fetchall(), "\n")
con.commit()    

#  Total number of students
print("Total number of students...")
stu_count = cur.execute("SELECT COUNT(*) FROM Student")
print(stu_count.fetchall(), "\n")
con.commit()

print("\n-------------------------------\n")

# -----------------------------------
# Task 8: Combining Conditions
# -----------------------------------
# Age > 15 **AND** marks > 70
print("Students age >= 21 AND marks > 90...")
result = cur.execute("SELECT * FROM Student WHERE AGE >= 21 AND MARKS > 90")
print(result.fetchall(), "\n")
con.commit()

# Age < 18 **OR** marks < 90
print("Students with AGE > 22 OR MARKS > 90...")
stu_age = cur.execute("SELECT * FROM Student WHERE AGE > 22 OR MARKS > 90")
print(stu_age.fetchall(), "\n")
con.commit()

print("\n-------------------------------\n")

# -----------------------------------
# Task 9: Handling NULL & UNIQUE Email
# -----------------------------------
# # Add a column `Email` (TEXT, UNIQUE, can be NULL).
# print("Adding unique email column...\n")
# cur.execute("ALTER TABLE Student ADD COLUMN EMAIL TEXT")
# con.commit()

# # Apply UNIQUE constraint
# cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_student_email ON Student(email)")
# con.commit()
# print("Email column added with UNIQUE constraint.\n")

# Insert a student with no email.
print("Inserting a student with no email...")
# cur.execute("INSERT INTO Student (NAME, AGE, MARKS, EMAIL) VALUES ('Alice', 21, 88.0, NULL)")
stu_insert_no_email_data = cur.execute("SELECT * FROM Student WHERE NAME = 'Alice'")
print(stu_insert_no_email_data.fetchall())
con.commit()

# # Try inserting two students with the same email (should fail).
# print("Inserting two students with SAME email to test UNIQUE...")
# try:
#     cur.execute("INSERT INTO Student (NAME, AGE, MARKS, EMAIL) VALUES ('Alice', 19, 85, 'alice@gmail.com')")
#     con.commit()

#     # Duplicate email → should FAIL
#     cur.execute("INSERT INTO Student (NAME, AGE, MARKS, EMAIL) VALUES ('Mia', 18, 88, 'alice@gmail.com')")
#     con.commit()

# except sqlite3.IntegrityError:
#     print("UNIQUE constraint WORKING — duplicate email rejected.\n")

print("\n-------------------------------\n")

# # -----------------------------------
# # Task 10: Delete Database File
# # -----------------------------------
print("Closing and deleting database...\n")
con.close()
# # os.remove('School.db')  # Delete the database file
# # print("Database file deleted successfully.")
