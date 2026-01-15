import sqlite3

con = sqlite3.connect('03_View.db')
cur = con.cursor()

cur.execute("PRAGMA foreign_keys = ON")

print("Connected to Transaction database sucessfully...")

print("\n---------------------------------\n")

cur.execute("""
    CREATE TABLE IF NOT EXISTS STUDENT(
            S_ID INTEGER PRIMARY KEY,
            S_NAME TEXT,
            S_CITY TEXT,
            S_MARKS INTEGER
        )
""")
con.commit()
print("Table created successfully...")

# cur.execute("""
#     INSERT INTO STUDENT (S_ID, S_NAME, S_CITY, S_MARKS) VALUES
#         (1, 'Raj', 'Surat', 85),
#         (2, 'Priya', 'Mumbai', 92),
#         (3, 'Arjun', 'Delhi', 76)
# """)
# con.commit()
print("Student table data inserted successfully...")

print("\n-------------------------\n")

cur.execute("""
    CREATE TABLE IF NOT EXISTS COURSE(
            C_ID INTEGER PRIMARY KEY,
            STUDENT_ID INTEGER,
            C_SUBJECT TEXT,
            FOREIGN KEY(STUDENT_ID) REFERENCES STUDENT(S_ID) ON DELETE CASCADE
        )
""")
con.commit()
print("Course table created successfully...")

# cur.execute("""
# INSERT INTO COURSE (C_ID, STUDENT_ID, C_SUBJECT) VALUES
#     (1, 1, 'Maths'),
#     (2, 2, 'Physics'),
#     (3, 1, 'Chemistry')
# """)
# con.commit()
print("Course table data inserted successfully...")

# --------------------------------
# View for high scorers
# --------------------------------
# cur.execute("""
#     CREATE VIEW VIEW_HIGH_SCORE AS 
#             SELECT S_NAME, S_CITY, S_MARKS FROM STUDENT WHERE S_MARKS >= 80
# """)
# con.commit()
cur.execute("SELECT * FROM VIEW_HIGH_SCORE")
print("\nShow high scores student ")
row = cur.fetchall()
for name, city, marks in row:
    print(f" - {name}, {city}, {marks}")
con.commit()

# --------------------------------
# Hide sensitive data:    Create view without ID:
# --------------------------------
# cur.execute("""
#     CREATE VIEW VIEW_STU_PUBLIC AS
#         SELECT S_NAME, S_CITY FROM STUDENT
# """)
# con.commit()
cur.execute("SELECT * FROM VIEW_STU_PUBLIC")
print("\nShow NAME and CITY from student table...")
row = cur.fetchall()
for name, city in row:
    print(f" - {name}, {city}")
con.commit()

# --------------------------------
# View for Report (JOINS)
# --------------------------------
# cur.execute("""
#     CREATE VIEW VIEW_STU_COURSE AS
#         SELECT S_NAME, C_SUBJECT FROM STUDENT
#     JOIN COURSE ON STUDENT.S_ID = COURSE.STUDENT_ID;
# """)
# con.commit()
cur.execute("SELECT * FROM VIEW_STU_COURSE")
print("\nShow NAME and SUBJECT from student and course table...")
row = cur.fetchall()
for name, course in row:
    print(f" - {name}, {course}")
con.commit()

con.close()


