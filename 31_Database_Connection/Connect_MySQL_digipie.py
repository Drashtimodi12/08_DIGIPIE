import mysql.connector

try:
    # Step 0: Establish connection to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dr@shti12",
        # database="digipie"
    )

    if conn.is_connected():
        print("Connection to MySQL digipie database was successful.")

except Exception as e:
    print("An error occurred while connecting to the database:", e)

finally:

    # Step 1: Create cursor and execute queries
    cursor  = conn.cursor()

    # Step 1: Create a new database
    cursor.execute("CREATE DATABASE IF NOT EXISTS digipie")
    print("\nDatabase 'digipie' created (or already exists).")

    # Step 2: Create employee table
    cursor.execute("USE digipie")  
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            NAME VARCHAR(50),
            AGE INT,
            MARKS INT
        )
    """)
    
    # Step 3: Insert new data into the employee table
    # cursor.execute("INSERT INTO EMPLOYEE (NAME, AGE, MARKS) VALUES ('SEJAL', 28, 9)")
    # conn.commit()
    # print("Data inserted successfully.")

    # Step 4: Fetch and display all records from the employee table
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()
    print("\nAll Employee Records:")
    for row in rows:
        print(row)
    
    # Step 5: Employees with marks > 7
    cursor.execute("SELECT * FROM employee WHERE MARKS > 7")
    rows = cursor.fetchall()
    print("\nEmployees with marks greater than 7:")
    for row in rows:
        print(row)

    # Step 6: Update marks for a specific employee
    cursor.execute("UPDATE employee SET MARKS = 1 WHERE ID = 3")
    conn.commit()
    print("\nMarks updated for employee 'Priyanshi'.")

    # Step 7: Delete an Employee Record
    cursor.execute("DELETE FROM employee WHERE ID = 10")
    conn.commit()      # Commit the changes
    print("\nEmployee with ID 10 deleted.")

    # Step 8: Count Total Employees
    cursor.execute("SELECT COUNT(*) from employee")
    total_employees = cursor.fetchone()[0]
    print("\nTotal number of employees:", total_employees)

    # Step 9: Find Average Marks
    cursor.execute("SELECT AVG(MARKS) from employee")
    average = cursor.fetchone()[0]     # Fetch the average marks 
    print("\nAverage marks of employees:", average)

    # Step 10: Sort Employees by Marks (Highest First)
    cursor.execute("SELECT * FROM employee order by MARKS DESC")
    rows = cursor.fetchall()
    print("\nEmployees sorted by marks (highest first):")
    for row in rows:
        print(row)

    # Step 11: Add a New Column (e.g., State)
    # cursor.execute("ALTER TABLE employee add column STATE varchar(50)")
    # conn.commit()
    # print("\nNew column 'STATE' added to employee table.")

    # Step 12: Update City Data
    cursor.execute("UPDATE employee SET CITY = 'Mumbai', STATE = 'Maharashtra' WHERE ID = 2")
    conn.commit()
    print("\nCity and State updated for employee with ID 2.")

    if conn.is_connected():
        cursor.close()
        conn.close()
        print("\nMySQL connection is closed.")