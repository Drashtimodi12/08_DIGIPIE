import sqlite3

con = sqlite3.connect('01_Transaction.db')
cur = con.cursor()

cur.execute("PRAGMA foreign_keys = ON")

print("Connected to Transaction database sucessfully...")

print("\n-------------------------------\n")

cur.execute("""
        CREATE TABLE IF NOT EXISTS CUSTOMER(
            C_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            C_NAME TEXT NOT NULL,
            C_ADDRESS TEXT NOT NULL,
            C_CONTACT INTEGER NOT NULL
        )
""")
con.commit()

# ON DELETE CASCADE → If customer is deleted → account also deletedcon.commit()
cur.execute("""
        CREATE TABLE IF NOT EXISTS ACCOUNT (
            A_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CUSTOMER_ID INTEGER NOT NULL,
            BALANCE REAL DEFAULT 0 CHECK (BALANCE >= 0),
            FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER(C_ID) ON DELETE CASCADE
        )
""")
print("CUSTOMER and ACCOUNT table created sucessfully...")

print("\n-------------------------------\n")

# cur.execute("""
#         INSERT INTO CUSTOMER (C_NAME, C_ADDRESS, C_CONTACT) VALUES
#             ('Aditi', 'Surat', 9876543210),
#             ('Rahul', 'Ahmedabad', 9123456780),
#             ('Priya', 'Ahmedabad', 9122334455) 
# """)
# con.commit()
print("CUSTOMER table data inserted successfully...")

print("\n-------------------------------\n")

# cur.execute("""
#     INSERT INTO ACCOUNT (CUSTOMER_ID, BALANCE) VALUES
#     (1, 5000.0),
#     (2, 10000.0),
#     (3, 12000.0)
# """)
# con.commit()
print("ACCOUNT table data inserted successfully...")

print("\n-------------------------------\n")



# -------------------------
# Transaction Task 1 → Money Transfer
# Transfer ₹1000 from Aditi → Priya
# -------------------------
# try:
#     cur.execute("BEGIN")        # Start transaction
    
#     cur.execute("UPDATE ACCOUNT SET BALANCE = BALANCE - 1000 WHERE A_ID = 1")
#     cur.execute("UPDATE ACCOUNT SET BALANCE = BALANCE + 1000 WHERE A_ID = 2")

#     con.commit()    # Save 

#     print("Transfer successful!")

# except Exception as e:
#     con.rollback()   # UNDO
#     print(e)
# print("\n-------------------------------\n")


# -------------------------
# Transaction Task 2 → Deposit Money
# Deposit ₹2000 into Aditi account
# -------------------------
# try:
#     cur.execute("BEGIN")        # Start transaction
#     cur.execute("UPDATE ACCOUNT SET BALANCE = BALANCE + 2000 WHERE A_ID = 1")
#     con.commit()    # Save 

#     print("Deposit successful!")

# except Exception as e:
#     con.rollback()   # UNDO
#     print(e)
# print("\n-------------------------------\n")



# -------------------------
# Transaction Task 3 → Withdraw Money
# Withdraw ₹1500 from Priya’s account
# -------------------------
# try:
#     cur.execute("BEGIN")
#     cur.execute("UPDATE ACCOUNT SET BALANCE = BALANCE - 1500 WHERE A_ID = 3")

#     con.commit()
#     print("Withdraw 1500 rs sucessfully from priyas account...")
# except Exception as e:
#     con.rollback()   # UNDO
#     print(e)
# print("\n-------------------------------\n")



# -------------------------
# ROLLBACK      We will try an invalid operation → negative deposit
# This should fail and revert everything.
# -------------------------
try:
    BALANCE = -1500  # user entered amount
    if BALANCE < 0:
        raise Exception("Negative deposit not allowed!")  # force error
    
    cur.execute("BEGIN")
    cur.execute("UPDATE ACCOUNT SET BALANCE = BALANCE + ? WHERE A_ID = 3", (BALANCE,))
    con.commit()
    print("Deposit -1500 rs sucessfully from priyas account...")
except Exception as e:
    con.rollback()   # UNDO
    print(e)
print("\n-------------------------------\n")


# -------------------------
# COMMIT     A simple valid insert
# -------------------------
# try:
#     cur.execute("BEGIN")
#     cur.execute("INSERT INTO CUSTOMER (C_NAME, C_ADDRESS, C_CONTACT) VALUES ('Drashti', 'Surat', 9834237813)")
#     con.commit()
#     print("Customer added...")
# except Exception as e:
#     con.rollback()
#     print(e)
# print("\n-------------------------------\n")


# -------------------------
# SHOW FINAL BALANCES
# -------------------------
try:
    cur.execute("BEGIN")
    cur.execute("""
        SELECT CUSTOMER.C_NAME, ACCOUNT.BALANCE FROM CUSTOMER
                LEFT JOIN ACCOUNT ON CUSTOMER.C_ID = ACCOUNT.CUSTOMER_ID
    """)
    row = cur.fetchall()
    con.commit()
    print("All customers and there account balance: ")
    for name, bal in row:
        print(f" - {name}, {bal}")
except Exception as e:
    con.rollback()
    print(e)


con.close()

