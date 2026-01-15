import sqlite3

con = sqlite3.connect('Classes.db')
cur = con.cursor()
print("\n=== CLASSES DATABASE ===\n")

print("\n-------------------------------\n")

cur.execute("""
        CREATE TABLE IF NOT EXISTS STUDENT (
            S_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            S_NAME TEXT NOT NULL,
            S_CITY TEXT NOT NULL
        )
    """)
con.commit()
print("Student table created successfully.")

# cur.execute("""
#         INSERT INTO STUDENT (S_NAME, S_CITY) VALUES
#         ("Alice", "New York"),
#         ("Bob", "Los Angeles"),
#         ("Charlie", "Chicago"),
#         ("Diana", "Houston"),
#         ("Ethan", "Phoenix"),
#         ("Roze", "USA")
#     """)
# con.commit()
print("Students inserted successfully.")

print("\n-------------------------------\n")

cur.execute("""
        CREATE TABLE IF NOT EXISTS COURSE (
            C_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            STUDENT_ID INTEGER NOT NULL,
            C_NAME TEXT NOT NULL,
            FOREIGN KEY (STUDENT_ID) REFERENCES STUDENT(S_ID)
        )
    """)
con.commit()
print("Course table created successfully.")

# cur.execute("""
#         INSERT INTO COURSE (STUDENT_ID, C_NAME) VALUES
#         (1, "Mathematics"),
#         (2, "Physics"),
#         (3, "Chemistry"),
#         (4, "Biology"),
#         (5, "History"),
#         (4, "Mathematics"),
#         (4, "Physics"),
#         (1, "Chemistry"),
#     """)
# con.commit()
print("Courses inserted successfully.")

print("\n-------------------------------\n")

# 1. INNER JOIN — students who have at least one course
cur.execute("""
        SELECT STUDENT.S_NAME, COURSE.C_NAME FROM STUDENT
            INNER JOIN COURSE ON STUDENT.S_ID = COURSE.STUDENT_ID
""")
row = cur.fetchall()
con.commit()
print("(INNER JOIN) Students and their courses (if any)...\n", row)
# (INNER JOIN) Students and their courses (if any)...
#  [('Alice', 'Mathematics'), ('Bob', 'Physics'), ('Charlie', 'Chemistry'), ('Diana', 'Biology'), ('Ethan', 'History'), ('Diana', 'Mathematics'), ('Diana', 'Physics'), ('Alice', 'Chemistry')]

print("\n-------------------------------\n")

# 2. LEFT JOIN — all students, even if no course
cur.execute("""
        SELECT STUDENT.S_NAME, COURSE.C_NAME FROM STUDENT
            LEFT JOIN COURSE ON STUDENT.S_ID = COURSE.STUDENT_ID
""")
row = cur.fetchall()
con.commit()
print("(LEFT JOIN) All students and their courses (if any)...\n", row)
# (LEFT JOIN) All students and their courses (if any)...
#  [('Alice', 'Chemistry'), ('Alice', 'Mathematics'), ('Bob', 'Physics'), ('Charlie', 'Chemistry'), ('Diana', 'Biology'), ('Diana', 'Mathematics'), ('Diana', 'Physics'), ('Ethan', 'History')]

print("\n-------------------------------\n")

# 3. RIGHT JOIN simulation (use LEFT JOIN reversed)      Students who have no course:
cur.execute("""
        SELECT COURSE.C_NAME, STUDENT.S_NAME FROM STUDENT
            LEFT JOIN COURSE ON STUDENT.S_ID = COURSE.STUDENT_ID 
            WHERE COURSE.C_NAME IS NULL
""")
row = cur.fetchall()
con.commit()
print("(RIGHT JOIN simulation) Students with no courses...\n", row)
# (RIGHT JOIN simulation) Students with no courses...
#  [(None, 'Roze')]

print("\n-------------------------------\n")

# 4. FULL JOIN simulation — all students and their courses
cur.execute("""
        SELECT STUDENT.S_NAME, COURSE.C_NAME FROM STUDENT
            LEFT JOIN COURSE ON STUDENT.S_ID = COURSE.STUDENT_ID
        UNION
        SELECT STUDENT.S_NAME, COURSE.C_NAME FROM COURSE
            LEFT JOIN STUDENT ON COURSE.STUDENT_ID = STUDENT.S_ID
""")
row = cur.fetchall()
con.commit()
print("(FULL JOIN simulation) All students and their courses...\n", row)
# (FULL JOIN simulation) All students and their courses...
#  [('Alice', 'Chemistry'), ('Alice', 'Mathematics'), ('Bob', 'Physics'), ('Charlie', 'Chemistry'), ('Diana', 'Biology'), ('Diana', 'Mathematics'), ('Diana', 'Physics'), ('Ethan', 'History'), ('Roze', None)]

print("\n-------------------------------\n")

# 5. CROSS JOIN - Cartesian product of students and courses
cur.execute("""
        SELECT STUDENT.S_NAME, COURSE.C_NAME FROM STUDENT
            CROSS JOIN COURSE
""")
row = cur.fetchall()
con.commit()
print("(CROSS JOIN) Cartesian product of students and courses...\n", row)
# (CROSS JOIN) Cartesian product of students and courses...
#  [('Alice', 'Mathematics'), ('Alice', 'Physics'), ('Alice', 'Chemistry'), ('Bob', 'Mathematics'), ('Bob', 'Physics'), ('Bob', 'Chemistry'), ('Charlie', 'Mathematics'), ('Charlie', 'Physics'), ('Charlie', 'Chemistry'), ('Diana', 'Mathematics'), ('Diana', 'Physics'), ('Diana', 'Chemistry'), ('Ethan', 'Mathematics'), ('Ethan', 'Physics'), ('Ethan', 'Chemistry'), ('Roze', 'Mathematics'), ('Roze', 'Physics'), ('Roze', 'Chemistry')]

print("\n-------------------------------\n")

# Print output in Python     Write your Python script to print all results nicely.
print("(FULL JOIN simulation) All students and their courses (formatted)...")
for name, course in row:
    if course == None:
        course = "No Course"
    print(f" - Student: {name}, {course}")



print("\n-------------------------------\n")

    
con.close()

