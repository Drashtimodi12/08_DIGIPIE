import sqlite3

con = sqlite3.connect('View_college.db')
cur = con.cursor()
print("\n-----College Database Connected-----\n")

cur.execute('PRAGMA foreign_keys = ON')

# -----------------------------------------
# STUDENT TABLE
# -----------------------------------------
cur.execute("""
        CREATE TABLE IF NOT EXISTS STUDENT (
            S_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            S_NAME TEXT NOT NULL, 
            S_CITY TEXT NOT NULL, 
            S_YEAR INTEGER NOT NULL
        ) 
    """)
con.commit()
print("Student table created successfully...")

# cur.execute("""
#     INSERT INTO STUDENT (S_NAME, S_CITY, S_YEAR) VALUES
#         ('Aarav Patel', 'Surat', 2022),
#         ('Neha Shah', 'Ahmedabad', 2021),
#         ('Rohit Mehta', 'Vadodara', 2023),
#         ('Priya Joshi', 'Rajkot', 2022),
#         ('Karan Desai', 'Surat', 2024),
#         ('Isha Trivedi', 'Mumbai', 2021),
#         ('Jatin Parmar', 'Pune', 2023),
#         ('Simran Kaur', 'Delhi', 2022),
#         ('Meera Rana', 'Chennai', 2024),
#         ('Harsh Gupta', 'Kolkata', 2023)
# """)
# con.commit()
print("Student all details inserted successfully...")

print("\n---------------------------------------\n")

# -----------------------------------------
# COURSE TABLE
# -----------------------------------------
cur.execute("""
      CREATE TABLE IF NOT EXISTS COURSE(
            C_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            STU_ID INTEGER,
            C_SUBJECT TEXT NOT NULL,
            C_MARKS INTEGER CHECK(C_MARKS >= 0 AND C_MARKS <= 100),
            FOREIGN KEY (STU_ID) REFERENCES STUDENT(S_ID) ON DELETE CASCADE 
        )
    """)
con.commit()
print("Course table created successfully...")

# cur.execute("""
#     INSERT INTO COURSE (STU_ID, C_SUBJECT, C_MARKS) VALUES
#         (1, 'Python', 85),
#         (2, 'DBMS', 78),
#         (3, 'C Programming', 91),
#         (4, 'Java', 65),
#         (5, 'HTML & CSS', 88),
#         (6, 'Machine Learning', 72),
#         (7, 'Django', 80),
#         (8, 'Data Structures', 69),
#         (9, 'Computer Networks', 94),
#         (10, 'Operating Systems', 76)
# """)
# con.commit()
print("Course and student id all details inserted successfully...")

print("\n---------------------------------------\n")

# -----------------------------------------
# FEES TABLE
# -----------------------------------------
cur.execute("""
        CREATE TABLE IF NOT EXISTS FEES (
            F_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            STU_ID INTEGER NOT NULL,
            TOTAL_FEE REAL NOT NULL CHECK(TOTAL_FEE >= 0),
            PAID_FEE REAL NOT NULL CHECK(PAID_FEE >= 0 AND PAID_FEE <= TOTAL_FEE),
            FOREIGN KEY (STU_ID) REFERENCES STUDENT(S_ID) ON DELETE CASCADE
        )
    """)
con.commit()
print("Fees table created successfully...")

# cur.execute("""
# INSERT INTO FEES (STUDENT_ID, TOTAL_FEE, PAID_FEE) VALUES
# (1, 50000, 30000),
# (2, 45000, 45000),
# (3, 60000, 40000),
# (4, 52000, 20000),
# (5, 48000, 48000),
# (6, 70000, 35000),
# (7, 55000, 30000),
# (8, 62000, 50000),
# (9, 75000, 75000),
# (10, 50000, 25000)
# """)
# con.commit()
print("Fees and student id all details inserted successfully...")

print("\n---------------------------------------\n")

# High Scoring Students    Show students who scored 80+ marks in any subject.
cur.execute("""
    CREATE VIEW IF NOT EXISTS VIEW_HIGH_MARKS AS 
            SELECT STUDENT.S_NAME, COURSE.C_SUBJECT, COURSE.C_MARKS FROM STUDENT
              JOIN COURSE ON STUDENT.S_ID = COURSE.STU_ID 
                  WHERE COURSE.C_MARKS >= 80
""")
con.commit()

cur.execute("SELECT * FROM VIEW_HIGH_MARKS")
print("Student who has 80+ marks: ")
row = cur.fetchall()
for name, subj, marks in row:
    print(f" - {name}, {subj}, {marks}")
con.commit()

print("\n---------------------------------------\n")

# Students Who Paid Full Fees
cur.execute("""
    CREATE VIEW IF NOT EXISTS VIEW_FULL_FEES_PAID AS
            SELECT STUDENT.S_NAME, FEES.TOTAL_FEE, FEES.PAID_FEE FROM STUDENT
                JOIN FEES ON STUDENT.S_ID = FEES.STU_ID 
                    WHERE FEES.TOTAL_FEE = PAID_FEE
""")
con.commit()

cur.execute("SELECT * FROM VIEW_FULL_FEES_PAID")
print("Student who has full paid fees: ")
row = cur.fetchall()
for name, total, paid in row:
    print(f" - {name}, {total}, {paid}")
con.commit()

print("\n---------------------------------------\n")

# Public Student Info (Hide Fees & Marks)
cur.execute("""
    CREATE VIEW IF NOT EXISTS VIEW_PUBLIC_STU_DETAILS AS
            SELECT S_NAME, S_CITY, S_YEAR FROM STUDENT
""")
con.commit()
cur.execute("SELECT * FROM VIEW_PUBLIC_STU_DETAILS")
print("Public Student details: ")
row = cur.fetchall()
for name, city, year in row:
    print(f" - {name}, {city}, {year}")
con.commit()

print("\n---------------------------------------\n")

# Complete Report View (JOIN of all tables)
cur.execute("""
    CREATE VIEW IF NOT EXISTS VIEW_COMPLETE_REPORT AS
        SELECT STUDENT.S_NAME, STUDENT.S_CITY, COURSE.C_SUBJECT, COURSE.C_MARKS, FEES.TOTAL_FEE, FEES.PAID_FEE 
        FROM STUDENT
            LEFT JOIN COURSE ON STUDENT.S_ID = COURSE.STU_ID
            LEFT JOIN FEES ON STUDENT.S_ID = FEES.STU_ID
""")
con.commit()

cur.execute("SELECT * FROM VIEW_COMPLETE_REPORT")
print("Complete student report: ")
row = cur.fetchall()
for name, city, sub, mark, total_fee, paid_fee in row:
    print(f" - {name}, {city}, {sub}, {mark}, {total_fee}, {paid_fee}")
con.commit()


# Update base table and check if view updates automatically
cur.execute("UPDATE STUDENT SET S_CITY = 'Vadodara' WHERE S_ID = 1")
con.commit()
cur.execute("SELECT * FROM VIEW_PUBLIC_STU_DETAILS")
print("Public Student details: ")
row = cur.fetchall()
for name, city, year in row:
    print(f" - {name}, {city}, {year}")
con.commit()















con.close()
