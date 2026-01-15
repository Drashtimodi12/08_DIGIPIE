from tkinter import *
from tkinter import messagebox
import mysql.connector

# Create the main application window
root = Tk()
root.geometry("500x600")  # Set window size to 500x600
root.title("Registration Form")  # Set the window title

# Function to submit form data to MySQL database
def submit_data():
    # Get input values from the form
    name = e1.get()
    contact = e2.get()
    email = e3.get()
    gender = e4.get()
    city = e5.get()
    state = e6.get()

    # Validate that no fields are left empty
    if name == "" or contact == "" or email == "" or gender == "" or city == "" or state == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    # Connect to the MySQL database (make sure credentials and database exist)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dr@shti12",
        port=3306,
        database="sql_query"
    )
    cursor = mydb.cursor()

    # SQL query to insert data into registration table
    sql = "INSERT INTO registration (name, contact, email, gender, city, state) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (name, contact, email, gender, city, state)

    # Execute query and commit changes
    cursor.execute(sql, val)
    mydb.commit()

    # Show success message
    messagebox.showinfo("Success", "Data inserted successfully!")

    # Clear the form fields
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.set("")
    e5.delete(0, END)
    e6.delete(0, END)

# ------------------------ UI Design ------------------------

# Labels for form fields
Label(root, text="Name").place(x=100, y=50)
Label(root, text="Contact").place(x=100, y=100)
Label(root, text="Email").place(x=100, y=150)
Label(root, text="Gender").place(x=100, y=200)
Label(root, text="City").place(x=100, y=250)
Label(root, text="State").place(x=100, y=300)

# Input fields
e1 = Entry(root)
e1.place(x=200, y=50)

e2 = Entry(root)
e2.place(x=200, y=100)

e3 = Entry(root)
e3.place(x=200, y=150)

# Gender selection using radio buttons
e4 = StringVar()
Radiobutton(root, text="Male", variable=e4, value="Male").place(x=200, y=200)
Radiobutton(root, text="Female", variable=e4, value="Female").place(x=270, y=200)

e5 = Entry(root)
e5.place(x=200, y=250)

e6 = Entry(root)
e6.place(x=200, y=300)

# Submit button
Button(root, text="Submit", command=submit_data, width=15).place(x=200, y=350)

# Start the GUI loop
root.mainloop()
