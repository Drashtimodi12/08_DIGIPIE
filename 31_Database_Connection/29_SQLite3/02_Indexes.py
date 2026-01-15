import sqlite3
import time

con = sqlite3.connect('02_Indexes.db')
cur = con.cursor()
cur.execute('PRAGMA foreign_keys = ON')

print("\n=======INDEXES DATABASE CONNECTED=======\n")

cur.execute("""
    CREATE TABLE IF NOT EXISTS EMPLOYEE (
        EMP_ID INTEGER PRIMARY KEY,
        EMP_NAME TEXT,
        DEPARTMENT TEXT, 
        EMP_SALARY REAL,
        EMP_CITY TEXT
    )
""")
con.commit()
print("Employee table created successfully...")

# cur.execute("""
#     INSERT INTO employee (EMP_ID, EMP_NAME, DEPARTMENT, EMP_SALARY, EMP_CITY) VALUES
#     (1, 'Aarav', 'HR', 35000, 'Surat'),
#     (2, 'Neha', 'Finance', 42000, 'Ahmedabad'),
#     (3, 'Rohit', 'IT', 55000, 'Mumbai'),
#     (4, 'Priya', 'Sales', 38000, 'Pune'),
#     (5, 'Vivek', 'IT', 60000, 'Bangalore'),
#     (6, 'Kavita', 'Marketing', 45000, 'Delhi'),
#     (7, 'Jatin', 'Finance', 47000, 'Surat'),
#     (8, 'Simran', 'HR', 36000, 'Chennai'),
#     (9, 'Harsh', 'Sales', 33000, 'Kolkata'),
#     (10, 'Meera', 'IT', 58000, 'Ahmedabad'),
#     (11, 'Suresh', 'Marketing', 41000, 'Jaipur'),
#     (12, 'Anjali', 'HR', 34000, 'Surat'),
#     (13, 'Deepak', 'Finance', 52000, 'Mumbai'),
#     (14, 'Ritu', 'Sales', 39000, 'Delhi'),
#     (15, 'Tarun', 'IT', 61000, 'Hyderabad'),
#     (16, 'Isha', 'Marketing', 44000, 'Pune'),
#     (17, 'Gaurav', 'Finance', 50000, 'Chennai'),
#     (18, 'Tina', 'HR', 37000, 'Bangalore'),
#     (19, 'Karan', 'IT', 57000, 'Delhi'),
#     (20, 'Nidhi', 'Sales', 36000, 'Surat')
# """)
# con.commit()
print("Employee table data inserted successfully...")

print("\n------------------------------------\n")

# -------------------------------------
# Understand Query Without INDEX
# -------------------------------------
start = time.perf_counter()
cur.execute("SELECT * FROM employee WHERE EMP_CITY = 'Surat'")
print("Show data who city is 'Surat': ")
row = cur.fetchall()
for id, name, dep, salary, city in row:
    print(f" - {id}, {name}, {dep}, {salary}, {city}")
con.commit()

print("\n------------------------------------\n")

cur.execute("SELECT EMP_ID, EMP_NAME, EMP_SALARY FROM employee WHERE EMP_SALARY > 50000")
print("Show data who salary is greater than 50000: ")
row = cur.fetchall()
for id, name, salary in row:
    print(f" - {id}, {name}, {salary}")
con.commit()

print("\n------------------------------------\n")

cur.execute("SELECT * FROM EMPLOYEE WHERE DEPARTMENT = 'IT'")
print("Show data who DEPARTMENT is 'it': ")
row = cur.fetchall()
for id, name, dep, salary, city in row:
    print(f" - {id}, {name}, {dep}, {salary}, {city}")
con.commit()
end = time.perf_counter()

print("\n------------------------------------\n")

print(f"It takes {end - start} seconds...")

print("\n------------------------------------\n")

start_idx = time.perf_counter()

# -------------------------------------
# Create Index on city
# -------------------------------------
cur.execute("CREATE INDEX IF NOT EXISTS IDX_EMP_CITY ON EMPLOYEE(EMP_CITY)")

cur.execute("SELECT EMP_ID, EMP_NAME, EMP_CITY FROM employee WHERE EMP_CITY = 'Surat'")

print("Using indexes Show data who city is 'Surat': ")
row = cur.fetchall()
for id, name, city in row:
    print(f" - {id}, {name}, {city}")
con.commit()

print("\n------------------------------------\n")

# -------------------------------------
# Create Index on salary
# -------------------------------------
cur.execute("CREATE INDEX IF NOT EXISTS IDX_EMP_SALARY ON EMPLOYEE(EMP_SALARY)")

cur.execute("SELECT EMP_ID, EMP_NAME, EMP_SALARY FROM employee WHERE EMP_SALARY > 50000")
print("Using indexes Show data who salary is greater than 50000: ")
row = cur.fetchall()
for id, name, salary in row:
    print(f" - {id}, {name}, {salary}")
con.commit()

print("\n------------------------------------\n")

# -------------------------------------
# Multi-Column Index (Composite)    Index on (department, city):
# -------------------------------------
cur.execute("CREATE INDEX IF NOT EXISTS IDX_EMP_DEPARTMENT_CITY ON EMPLOYEE(DEPARTMENT, EMP_CITY)")

cur.execute("SELECT * FROM EMPLOYEE WHERE DEPARTMENT = 'IT' AND EMP_CITY = 'Ahmedabad'")
print("Using indexes Show data who department IT and city is Ahmedabad: ")
row = cur.fetchall()
for id, name, dep, salary, city in row:
    print(f" - {id}, {name}, {dep}, {salary}, {city}")
con.commit()
end = time.perf_counter()

# -------------------------------------
# Add unique index
# -------------------------------------
cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS IDX_EMP_NAME_UNIQUE ON EMPLOYEE(EMP_NAME)")

# cur.execute("""INSERT INTO EMPLOYEE (EMP_ID, EMP_NAME, DEPARTMENT, EMP_SALARY, EMP_CITY) VALUES
#         (21, 'Aarav', 'HR', 35000, 'Surat')""")
# print("Using unqiue indexes try to insert same data: ")
# con.commit()

end_idx = time.perf_counter()

# -------------------------------------
# Delete Index
# -------------------------------------
# try:
#     cur.execute("DROP INDEX IF EXISTS IDX_EMP_NAME_UNIQUE")
#     print("Index deleted successfully")
# except Exception as e:
#     print("Error:", e)

print("\n------------------------------------\n")

print(f"It takes {end_idx - start_idx} seconds...")

print("\n------------------------------------\n")
cur.execute("PRAGMA index_list('EMPLOYEE')")
print("Available Indexes: ")
indexes = cur.fetchall()
con.commit()
for idx in indexes:
    seq, name, unique, origin, partial = idx
    print(f"Index: {name} | Unique: {unique} | Origin: {origin} | Partial: {partial}")

con.close()