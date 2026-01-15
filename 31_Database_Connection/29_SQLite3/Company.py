import sqlite3

con = sqlite3.connect('Company.db')
cur = con.cursor()
print("\n=== COMPANY DATABASE ===\n")

print("\n-------------------------------\n")

# --------------------------
# create Department table
# --------------------------
cur.execute("""
        CREATE TABLE IF NOT EXISTS DEPARTMENT (
            DEPT_ID INTEGER PRIMARY KEY,
            DEPT_NAME TEXT NOT NULL )
""")
con.commit()
print("Department table created sucessfully...")

print("\n-------------------------------\n")

# cur.execute("""
#         INSERT INTO DEPARTMENT (DEPT_ID, DEPT_NAME) VALUES
#             (101, 'Legal'),
#             (102, 'Finance'),
#             (103, 'IT'),
#             (104, 'Marketing'),
#             (105, 'Sales'),
#             (106, 'HR')
# """)
# con.commit()
print("Department data inserted sucessfully...")

print("\n-------------------------------\n")


# --------------------------
# create Employee table
# --------------------------

cur.execute("""
        CREATE TABLE IF NOT EXISTS EMPLOYEE (
            EMP_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            EMP_NAME TEXT NOT NULL,
            DEPT_ID INTEGER,
            EMP_ADDRESS TEXT NOT NULL,
            FOREIGN KEY (DEPT_ID) REFERENCES DEPARTMENT (DEPT_ID)
        )
""")
con.commit()
print("Employee table created sucessfully...")

print("\n-------------------------------\n")

# cur.execute("""
#         INSERT INTO EMPLOYEE (EMP_NAME, DEPT_ID, EMP_ADDRESS) VALUES
#                 ('Raj Patel', 103, 'Ahmedabad'),
#                 ('Priya Sharma', 105, 'Surat'),
#                 ('Amit Singh', 101, 'Vadodara'),
#                 ('Kajal Mehta', 101, 'Rajkot'),
#                 ('Dhruv Joshi', 104, 'Bhavnagar'),
#                 ('Sneha Rao', 103, 'Anand'),
#                 ('Manish Shah', 102, 'Nadiad'),
#                 ('Ritika Desai', 105, 'Gandhinagar'),
#                 ('Harshil Patel', 101, 'Mehsana'),
#                 ('Neha Verma', 105, 'Junagadh')
# """)
# con.commit()
print("Employee data inserted sucessfully...")

print("\n-------------------------------\n")



# --------------------------
# Inner Join  Employees + their correct department names
# --------------------------
cur.execute("""
        SELECT EMPLOYEE.EMP_NAME, EMPLOYEE.EMP_ADDRESS, DEPARTMENT.DEPT_NAME 
        FROM EMPLOYEE
            INNER JOIN DEPARTMENT ON EMPLOYEE.DEPT_ID = DEPARTMENT.DEPT_ID 
""")
row = cur.fetchall()
print("EMPLOYEE TABLE INNER JOIN DEPARTMENT TABLE...")
for ename, eadd, dname in row:
    print(f" - {ename}, {dname}, {eadd}")

print("\n-------------------------------\n")

# --------------------------
# LEFT JOIN (All employees, even if no department)
# --------------------------
cur.execute("""
        SELECT EMPLOYEE.EMP_NAME, EMPLOYEE.EMP_ADDRESS, DEPARTMENT.DEPT_NAME 
        FROM EMPLOYEE
            LEFT JOIN DEPARTMENT ON EMPLOYEE.DEPT_ID = DEPARTMENT.DEPT_ID 
""")
row = cur.fetchall()
print("EMPLOYEE TABLE LEFT JOIN DEPARTMENT TABLE...")
for ename, eadd, dname in row:
    print(f" - {ename}, {dname}, {eadd}")

print("\n-------------------------------\n")


# --------------------------
# RIGHT JOIN Simulation (Departments with no employees)
# --------------------------
cur.execute("""
        SELECT DEPARTMENT.DEPT_NAME
        FROM DEPARTMENT
        LEFT JOIN EMPLOYEE ON DEPARTMENT.DEPT_ID = EMPLOYEE.DEPT_ID
        WHERE EMPLOYEE.EMP_ID IS NULL
""")
rows = cur.fetchall()
print("DEPARTMENT TABLE LEFT JOIN EMPLOYEE TABLE...")
if rows:
    for dept in rows:
        print(f" - {dept}")
else:
    print("All departments have employees.")

print("\n-------------------------------\n")

# --------------------------
# FULL JOIN Simulation (Employees + all departments)
# --------------------------
cur.execute("""
        SELECT EMPLOYEE.EMP_NAME, DEPARTMENT.DEPT_NAME 
            FROM EMPLOYEE
            LEFT JOIN DEPARTMENT ON EMPLOYEE.DEPT_ID = DEPARTMENT.DEPT_ID
        UNION
        SELECT EMPLOYEE.EMP_NAME, DEPARTMENT.DEPT_NAME
            FROM DEPARTMENT
            LEFT JOIN EMPLOYEE ON DEPARTMENT.DEPT_ID = EMPLOYEE.DEPT_ID
""")
row = cur.fetchall()
print("FULL JOIN DEPARTMENT AND EMPLOYEE TABLE")
for ename, dname in row:
    print(f" - {ename}, {dname}")

print("\n-------------------------------\n")


con.close()