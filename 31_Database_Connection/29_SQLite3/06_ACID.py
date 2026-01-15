import sqlite3

con = sqlite3.connect("06_ACID.db")
cur = con.cursor()

print("\n===== ACID PROPERTIES PRACTICAL =====\n")

# ---------------------------------------
# 1. Create Tables
# ---------------------------------------
cur.execute("""
    CREATE TABLE IF NOT EXISTS ACCOUNT(
        AC_ID INTEGER PRIMARY KEY,
        AC_NAME TEXT,
        BALANCE INTEGER CHECK(BALANCE >= 0)
    )
""")

# # Insert initial balances
# cur.execute("INSERT INTO ACCOUNT (AC_ID, AC_NAME, BALANCE) VALUES (1, 'Alice', 1000), (2, 'Bob', 500)")
# con.commit()

print("Initial Data Inserted.\n")


# -------------------------------------------------------
# ATOMICITY PRACTICAL
# -------------------------------------------------------
print("===== 1. ATOMICITY TEST =====")

try:
    con.execute("BEGIN")  # Start transaction

    # 1. Deduct from Alice
    cur.execute("UPDATE ACCOUNT SET BALANCE = BALANCE - 600 WHERE AC_ID = 1")

    # 2. Add to Bob (Introduce ERROR to test rollback)
    # Bob column name is wrong --> will cause error
    cur.execute("UPDATE ACCOUNT SET BALANCe_WRONG = BALANCE + 600 WHERE AC_ID = 2")  

    con.commit()  # Will NOT run due to error
except Exception as e:
    print("Error Occurred:", e)
    con.rollback()
    print("Transaction ROLLED BACK due to error.")

# Check data after atomicity test
cur.execute("SELECT * FROM ACCOUNT")
print("\nAccount Table After Atomicity Test:")
for row in cur.fetchall():
    print(row)

# Alice should still have 1000 (not deducted)
# Bob should still have 500


# -------------------------------------------------------
# CONSISTENCY PRACTICAL
# -------------------------------------------------------
print("\n===== 2. CONSISTENCY TEST =====")

try:
    con.execute("BEGIN")

    # Try making balance negative (violates CHECK constraint)
    cur.execute("UPDATE ACCOUNT SET BALANCE = -200 WHERE AC_ID = 1")

    con.commit()
except Exception as e:
    print("Consistency Error:", e)
    con.rollback()

cur.execute("SELECT * FROM ACCOUNT")
print("\nAccount Table After Consistency Test:")
for row in cur.fetchall():
    print(row)

# Balance remains unchanged because negative values violate rule


# -------------------------------------------------------
# ISOLATION PRACTICAL
# -------------------------------------------------------
print("\n===== 3. ISOLATION TEST (FIXED) =====")

# Enable WAL mode (allows read while writing)
con_main = sqlite3.connect("06_ACID.db")
con_main.execute("PRAGMA journal_mode=WAL;")
con_main.close()

# Open two connections with DEFERRED mode
con1 = sqlite3.connect("06_ACID.db", isolation_level="DEFERRED")
con2 = sqlite3.connect("06_ACID.db", isolation_level="DEFERRED")

cur1 = con1.cursor()
cur2 = con2.cursor()

# Start Transaction 1
print("\n--- Transaction 1 started ---")
cur1.execute("BEGIN;")
cur1.execute("UPDATE ACCOUNT SET BALANCE = BALANCE + 100 WHERE AC_ID = 1")
print("Transaction 1 updated balance but NOT committed yet.")

# Start Transaction 2 (read only)
print("\n--- Transaction 2 started ---")
cur2.execute("BEGIN;")
cur2.execute("SELECT BALANCE FROM ACCOUNT WHERE AC_ID = 1")
print("Transaction 2 sees balance as:", cur2.fetchone()[0])

# Commit Transaction 1
print("\n--- Committing Transaction 1 ---")
con1.commit()

# Now Transaction 2 reads again
cur2.execute("SELECT BALANCE FROM ACCOUNT WHERE AC_ID = 1")
print("Transaction 2 after T1 commit:", cur2.fetchone()[0])

# Commit Transaction 2
con2.commit()

con1.close()
con2.close()

# -------------------------------------------------------
# DURABILITY PRACTICAL
# -------------------------------------------------------
print("\n===== 4. DURABILITY TEST =====")

cur.execute("UPDATE ACCOUNT SET BALANCE = BALANCE + 500 WHERE AC_ID = 2")
con.commit()
print("Data committed.")

print("Simulating system crash...")
con.close()  # Closing simulates sudden shutdown

# Re-open database to check durability
con = sqlite3.connect("06_ACID.db")
cur = con.cursor()

cur.execute("SELECT * FROM ACCOUNT")
print("\nData after restart (Durability):")
for row in cur.fetchall():
    print(row)

print("\n===== ACID PRACTICAL COMPLETED =====")
