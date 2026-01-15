import sqlite3
import os

print("\n=== ENROLLMENT DATABASE ===\n")

# -----------------------------------
# Task 1: Create Database & Table
# -----------------------------------
con = sqlite3.connect('05_Join.db')      # Connect to database (creates file if not exists)
cur = con.cursor()          # Create a cursor object. It helps to execute SQL queries in

cur.execute("PRAGMA foreign_keys = ON")

print("Connected to Enrollment database successfully.")

print("\n--------------------------------\n")

# -----------------------------------
# Create Student Table
# -----------------------------------
cur.execute('''
    CREATE TABLE IF NOT EXISTS Student (
        S_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        AGE INTEGER NOT NULL
    )
''')
con.commit()
print("Student Table created successfully.")

print("\n--------------------------------\n")

# -----------------------------------
# Insert Student Data
# -----------------------------------
# cur.execute("""
#         INSERT INTO Student (NAME, AGE) VALUES
#         ("ROZE", 22), 
#         ("MIKE", 21), 
#         ("ANNA", 23),
#         ("LUCY", 20), 
#         ("JAMES", 22), 
#         ("SOPHIA", 21),
#         ("DAVID", 23)
# """)
# con.commit()
# print("Student records inserted successfully.")

# print("\n--------------------------------\n")

# -----------------------------------
# Create Course Table
# -----------------------------------
cur.execute('''
        CREATE TABLE IF NOT EXISTS Course (
            C_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            COURSE_NAME TEXT NOT NULL)
''')
con.commit()
print("Course Table created successfully.")

print("\n--------------------------------\n")

# -----------------------------------
# Insert Course Data
# -----------------------------------
# cur.execute("""
#         INSERT INTO Course (COURSE_NAME) VALUES
#             ('Mchine Learning'),
#             ('Data Science'),
#             ('Database Management System'),
#             ('Operating System'),
#             ('Computer Networks')
# """)
# con.commit()
# print("Course records inserted successfully.")


# print("\n--------------------------------\n")

# -----------------------------------
# Create Enrollment Table
# -----------------------------------
cur.execute('''
        CREATE TABLE IF NOT EXISTS Enrollment (
            ENROLL_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            STUDENT_ID INTEGER ,
            COURSE_ID INTEGER,
            FOREIGN KEY (STUDENT_ID) REFERENCES Student(S_ID),
            FOREIGN KEY (COURSE_ID) REFERENCES Course(C_ID) ON DELETE CASCADE
        )
''')
# ON DELETE CASCADE → If student is deleted → enrollmetn also deleted
con.commit()
print("Enrollment Table created successfully.")

print("\n--------------------------------\n")

# -----------------------------------
# Insert Enrollment Data
# -----------------------------------
# cur.execute("""
#     INSERT INTO Enrollment (STUDENT_ID, COURSE_ID) VALUES
#         (1, 1),   -- ROZE → Machine Learning
#         (3, 4),   -- ANNA → Operating System
#         (2, 2),   -- MIKE → Data Science
#         (4, 3),   -- LUCY → DBMS
#         (7, 5)    -- DAVID → Computer Networks
# """)
# con.commit()
# print("Enrollment records inserted successfully.")

# print("\n--------------------------------\n")

# -----------------------------------
# Using a JOIN between Student, Course, Enrollment.
# -----------------------------------
# 1. INNER JOIN         Only matching data from both tables.
# Only students who are enrolled will appear.
# Enrollment join with student and enrollment join with course
cur.execute("""
        SELECT NAME, COURSE_NAME FROM ENROLLMENT
        INNER JOIN Student ON ENROLLMENT.STUDENT_ID = Student.S_ID
        INNER JOIN Course ON ENROLLMENT.COURSE_ID = Course.C_ID
""")
# Enrollment join with student only
# cur.execute("""
#         SELECT NAME, COURSE_ID FROM ENROLLMENT
#         INNER JOIN Student ON ENROLLMENT.STUDENT_ID = Student.S_ID
# """)
rows = cur.fetchall()
con.commit()
print("INNER JOIN BETWEEN Student, Course, Enrollment...\n", rows)      # Only students who are enrolled will appear.

print("\n--------------------------------\n")

# 2. LEFT JOIN          All students, with enrolled courses if available.
# Students without any enrolled courses will show NULL for COURSE_NAME.
# Student left join with enrollment and enrollment left join with course
cur.execute("""
        SELECT Student.NAME, Course.COURSE_NAME FROM Student
        LEFT JOIN Enrollment ON Student.S_ID = Enrollment.STUDENT_ID
        LEFT JOIN Course ON Enrollment.COURSE_ID = Course.C_ID
""")
# Student left join with enrollment only
# cur.execute("""
#         SELECT Student.NAME, Enrollment.COURSE_ID FROM Student
#         LEFT JOIN Enrollment ON Student.S_ID = Enrollment.STUDENT_ID
# """)
rows = cur.fetchall()
con.commit()
print("LEFT JOIN BETWEEN Student, Enrollment...\n", rows)      # All students will appear, with NULL for those not enrolled.

print("\n--------------------------------\n")

# 3. RIGHT JOIN         
# Courses without any enrolled students will show NULL for NAME.
# Course right join with Enrollment and enrollment right join with student
cur.execute("""
        SELECT Course.COURSE_NAME, Student.NAME FROM Course
            LEFT JOIN Enrollment ON Course.C_ID = Enrollment.COURSE_ID
               LEFT JOIN  Student ON Enrollment.STUDENT_ID = Student.S_ID
""")
# Course right join with Enrollment only
# cur.execute("""
#         SELECT Course.COURSE_NAME, Enrollment.STUDENT_ID FROM Course
#             LEFT JOIN Enrollment ON Course.C_ID = Enrollment.COURSE_ID
# """)
rows = cur.fetchall()
con.commit()
print("RIGHT JOIN BETWEEN Course, Enrollment...\n", rows)      # All courses will appear, with NULL for those without students.

print("\n--------------------------------\n")

# 4. FULL OUTER JOIN — NOT SUPPORTED in SQLite      But we can simulate with UNION.
# All students and all courses, matching where possible.
# Student left join with enrollment and enrollment left join with course
cur.execute("""
        SELECT Student.NAME, Course.COURSE_NAME FROM Student
            LEFT JOIN Enrollment ON Student.S_ID = Enrollment.STUDENT_ID
                LEFT JOIN Course ON Enrollment.COURSE_ID = Course.C_ID
        UNION
        SELECT Student.NAME, Course.COURSE_NAME FROM Course
            LEFT JOIN Enrollment ON Course.C_ID = Enrollment.COURSE_ID
                LEFT JOIN Student ON Enrollment.STUDENT_ID = Student.S_ID;
""")
rows = cur.fetchall()
con.commit()
print("FULL OUTER JOIN BETWEEN Student, Course, Enrollment...\n", rows)

print("\n--------------------------------\n")

# 5. CROSS JOIN         All possible combinations of students and courses.
# Every student paired with every course.
# Student cross join with course
cur.execute("""
        SELECT Student.NAME, Course.COURSE_NAME FROM Student
        CROSS JOIN Course
""")
rows = cur.fetchall()
con.commit()
print("CROSS JOIN BETWEEN Student, Course...\n", rows)

print("\n--------------------------------\n")

# 5. SELF JOIN (Rare for this case)     Used when comparing a table to itself.
# Comparing students to other students.
# Student self join with student
cur.execute("""
        SELECT A.NAME AS Student_A, B.NAME AS Student_B FROM Student A
        JOIN Student B ON A.S_ID != B.S_ID
""")
rows = cur.fetchall()
con.commit()
print("SELF JOIN ON Student...\n", rows)

print("\n--------------------------------\n")

# 4. Show all students enrolled in “Computer Networks”
cur.execute("""
        SELECT NAME, COURSE_NAME FROM ENROLLMENT
        INNER JOIN Student ON ENROLLMENT.STUDENT_ID = Student.S_ID
        INNER JOIN Course ON ENROLLMENT.COURSE_ID = Course.C_ID
            WHERE Course.COURSE_NAME = 'Computer Networks'
""")
rows = cur.fetchall()
con.commit()
print("Student enrolled in Computer Networks...\n")
for name, course in rows:
    print(f" - {name} ({course})")

print("\n--------------------------------\n")

# 5. Show how many courses each student has enrolled in    (Hint: GROUP BY)
cur.execute("""
        SELECT Student.NAME, COUNT(Enrollment.COURSE_ID) AS COURSE_ENROLLED
            FROM Student
        LEFT JOIN Enrollment ON Student.S_ID = Enrollment.STUDENT_ID
        GROUP BY Student.S_ID, Student.NAME
""")
rows = cur.fetchall()
print("Number of courses each student is enrolled in:")
for name, count in rows:
    print(f" - {name}: {count}")

print("\n--------------------------------\n")

# 6. Show number of students in each course     (Hint: GROUP BY COURSE_NAME)
cur.execute("""
        SELECT Course.COURSE_NAME, COUNT(Enrollment.STUDENT_ID) AS STUDENT_ENROLLED
                FROM Course
        LEFT JOIN Enrollment ON Course.C_ID = Enrollment.COURSE_ID
            GROUP BY Course.C_ID, Course.COURSE_NAME
""")
rows = cur.fetchall()
print("Number of students enrolled in each course:")
for name, count in rows:
    print(f" - {name}: {count}")

print("\n--------------------------------\n")

# 7. Delete course 'Computer Networks' and ensure all enrollments linked to it are removed.
# cur.execute("""
#         DELETE FROM Course WHERE COURSE_NAME = 'Computer Networks'
# """)
# con.commit()

# 8. Update student name whose ID = 3
cur.execute("UPDATE STUDENT SET NAME='Daizy' WHERE S_ID = 3 ")
con.commit()

# 9. Show all students who are enrolled in more than 0 courses  (Hint: HAVING COUNT(*) > 0)
cur.execute("""
    SELECT Student.NAME, COUNT(Enrollment.COURSE_ID) AS TotalCourses
    FROM Student
    INNER JOIN Enrollment ON Student.S_ID = Enrollment.STUDENT_ID
    GROUP BY Student.S_ID, Student.NAME
    HAVING COUNT(Enrollment.COURSE_ID) > 0;
""")

rows = cur.fetchall()
print("Students enrolled in more than 2 courses:")
for name, total in rows:
    print(f" - {name}: {total} courses")


con.close()
