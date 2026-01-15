import sqlite3

# ---------------------------------------
# CONNECT TO DATABASE
# ---------------------------------------
con = sqlite3.connect('04_Trigger.db')
cur = con.cursor()

# ---------------------------------------
# CREATE STUDENT TABLE
# ---------------------------------------
cur.execute("""
    CREATE TABLE IF NOT EXISTS STUDENT (
        S_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        FIRST_NAME TEXT NOT NULL,
        LAST_NAME TEXT NOT NULL,
        CLASS TEXT NOT NULL CHECK(length(CLASS) = 2),
        SECTION TEXT
    )
""")

# ---------------------------------------
# SAMPLE DATA INSERTION (Optional)
# ---------------------------------------
cur.execute("""
    INSERT INTO STUDENT (FIRST_NAME, LAST_NAME, CLASS, SECTION) VALUES
        ('Raj', 'Patel', '10', 'A'),
        ('Priya', 'Shah', '09', 'B'),
        ('Amit', 'Mehta', '08', 'A'),
        ('Neha', 'Joshi', '07', 'C')
""")
con.commit()

# ============================================================
#               🔹 BEFORE INSERT TRIGGER
#       Validate FIRST_NAME and LAST_NAME must be alphabetic
# ============================================================
cur.execute("""
    CREATE TRIGGER IF NOT EXISTS BEFORE_INSERT_STUDENT
    BEFORE INSERT ON STUDENT
    BEGIN
        SELECT CASE
            WHEN NEW.FIRST_NAME GLOB '*[^A-Za-z]*'
              OR NEW.LAST_NAME GLOB '*[^A-Za-z]*'
            THEN
                RAISE(ABORT, 'ERROR: FirstName and LastName must contain alphabets only!')
        END;
    END;
""")

# ============================================================
#               🔹 BEFORE UPDATE TRIGGER
#     Validate CLASS must always be 2-digit (example: '07')
# ============================================================
cur.execute("""
    CREATE TRIGGER IF NOT EXISTS BEFORE_UPDATE_CLASS
    BEFORE UPDATE ON STUDENT
    FOR EACH ROW
    BEGIN
        SELECT CASE
            WHEN length(NEW.CLASS) != 2 THEN
                RAISE(ABORT, 'ERROR: CLASS must be exactly 2 characters (e.g., 07, 10)')
        END;
    END;
""")

# ============================================================
#      🔹 CREATE HISTORY TABLE FOR UPDATE LOGGING
# ============================================================
cur.execute("""
    CREATE TABLE IF NOT EXISTS STUDENT_HISTORY (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STUDENT_ID INTEGER,
        OLD_CLASS TEXT,
        NEW_CLASS TEXT,
        CHANGE_TIME TIMESTAMP
    )
""")

# ============================================================
#               🔹 AFTER UPDATE TRIGGER
#     Logs the old class & new class into history table
# ============================================================
cur.execute("""
    CREATE TRIGGER IF NOT EXISTS AFTER_UPDATE_CLASS
    AFTER UPDATE ON STUDENT
    FOR EACH ROW
    BEGIN
        INSERT INTO STUDENT_HISTORY
        VALUES (NULL, OLD.S_ID, OLD.CLASS, NEW.CLASS, DATETIME('now'));
    END;
""")

# ============================================================
#     🔹 CREATE DELETE HISTORY TABLE (AUDIT DELETE)
# ============================================================
cur.execute("""
    CREATE TABLE IF NOT EXISTS STUDENT_DELETE_HISTORY (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STUDENT_ID INTEGER,
        FIRST_NAME TEXT,
        LAST_NAME TEXT,
        CLASS TEXT,
        SECTION TEXT,
        DELETE_TIME TIMESTAMP
    )
""")

# ============================================================
#               🔹 BEFORE DELETE TRIGGER
#       Block delete of CLASS '10' students (Example rule)
# ============================================================
cur.execute("""
    CREATE TRIGGER IF NOT EXISTS BEFORE_DELETE_STUDENT
    BEFORE DELETE ON STUDENT
    BEGIN
        SELECT CASE
            WHEN OLD.CLASS = '10' THEN
                RAISE(ABORT, 'ERROR: Cannot delete CLASS 10 students!')
        END;
    END;
""")

# ============================================================
#               🔹 AFTER DELETE TRIGGER
#     Log deleted student's complete data into history table
# ============================================================
cur.execute("""
    CREATE TRIGGER IF NOT EXISTS AFTER_DELETE_STUDENT
    AFTER DELETE ON STUDENT
    BEGIN
        INSERT INTO STUDENT_DELETE_HISTORY
        VALUES (NULL, OLD.S_ID, OLD.FIRST_NAME, OLD.LAST_NAME, OLD.CLASS, OLD.SECTION, DATETIME('now'));
    END;
""")

con.commit()

# ============================================================
#                 🔹 TESTING AREA
#     Uncomment these lines to test every trigger
# ============================================================

# ---- Test BEFORE INSERT trigger (should fail)
# cur.execute("INSERT INTO STUDENT (FIRST_NAME, LAST_NAME, CLASS, SECTION) VALUES ('Riya123', 'Patel', '08', 'B')")

# ---- Test BEFORE UPDATE (should fail)
# cur.execute("UPDATE STUDENT SET CLASS='100' WHERE S_ID=1")

# ---- Test AFTER UPDATE (will log history)
# cur.execute("UPDATE STUDENT SET CLASS='11' WHERE S_ID=2")

# ---- Test BEFORE DELETE (should fail for CLASS 10)
# cur.execute("DELETE FROM STUDENT WHERE S_ID=1")

# ---- Test AFTER DELETE (log deletion)
# cur.execute("DELETE FROM STUDENT WHERE S_ID=3")

# con.commit()

# ============================================================
# Close connection
# ============================================================
con.close()

print("All tables and triggers created successfully!")
