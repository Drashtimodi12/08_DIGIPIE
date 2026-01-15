# Import necessary modules
from tkinter import *                 # For GUI elements
import mysql.connector                # For MySQL database connectivity
from tkinter import ttk              # For Treeview table widget
from tkinter import messagebox       # For showing popup messages

# Create main window
root = Tk()
root.geometry("800x500")             # Set window size
root.title("Student Registration")   # Set window title


# Function to establish MySQL connection
def conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dr@shti12",
        port=3306,
        database="sql_query"
    )


# Function to fetch data from the selected row and show in entry fields
def getdata(event):
    rowid = table.selection()[0]             # Get selected row ID
    rdata = table.item(rowid)['values']      # Fetch data from selected row
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e1.insert(0, rdata[0])                   # Insert ID into entry
    e2.insert(0, rdata[1])                   # Insert Name
    e3.insert(0, rdata[2])                   # Insert Email
    e4.insert(0, rdata[3])                   # Insert Phone


# Function to add new user into the database
def add():
    id = e1.get()
    name = e2.get()
    email = e3.get()
    phone = e4.get()
    con = conn()
    cursor = con.cursor()
    qry = "INSERT INTO users (id, name, email, phone) VALUES (%s, %s, %s, %s)"
    val = (id, name, email, phone)
    cursor.execute(qry, val)
    con.commit()
    con.close()
    clear_entries()                                  # Clear input fields
    messagebox.showinfo("Success", "User inserted successfully")
    refresh_table()                                  # Refresh table


# Function to update existing user data
def update():
    id = e1.get()
    name = e2.get()
    email = e3.get()
    phone = e4.get()
    con = conn()
    cursor = con.cursor()
    qry = "UPDATE users SET name=%s, email=%s, phone=%s WHERE id=%s"
    val = (name, email, phone, id)
    cursor.execute(qry, val)
    con.commit()
    con.close()
    clear_entries()
    messagebox.showinfo("Success", "User updated successfully")
    refresh_table()


# Function to delete user based on ID
def delete():
    id = e1.get()
    con = conn()
    cursor = con.cursor()
    qry = "DELETE FROM users WHERE id=%s"
    cursor.execute(qry, (id,))
    con.commit()
    con.close()
    clear_entries()
    messagebox.showinfo("Success", "User deleted successfully")
    refresh_table()


# Function to show all data in the table
def show():
    con = conn()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    con.close()

    last_id = 0
    for row in data:
        table.insert("", END, values=row)   # Insert each row into the table
        last_id = row[0]                    # Track last used ID

    e1.delete(0, END)
    e1.insert(0, last_id + 1)               # Auto-suggest next ID


# Function to clear table and reload data
def refresh_table():
    for item in table.get_children():       # Remove all rows
        table.delete(item)
    show()                                  # Reload from DB


# Function to clear all input fields
def clear_entries():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e1.focus_set()                          # Set cursor focus to ID field


# ---------- GUI ELEMENTS ----------

# Labels
Label(root, text="Id").place(x=10, y=10)
Label(root, text="Name").place(x=10, y=40)
Label(root, text="Email").place(x=10, y=70)
Label(root, text="Phone").place(x=10, y=100)

# Entry Fields
e1 = Entry(root)
e1.place(x=100, y=10)
e2 = Entry(root)
e2.place(x=100, y=40)
e3 = Entry(root)
e3.place(x=100, y=70)
e4 = Entry(root)
e4.place(x=100, y=100)

# Buttons for Add, Update, Delete
Button(root, text="Add", command=add, height=2, width=7).place(x=10, y=130)
Button(root, text="Update", command=update, height=2, width=7).place(x=90, y=130)
Button(root, text="Delete", command=delete, height=2, width=7).place(x=170, y=130)

# Table setup using Treeview
cols = ("Id", "Name", "Email", "Phone")
table = ttk.Treeview(root, columns=cols, show="headings")

for col in cols:
    table.heading(col, text=col)            # Set table column heading
    table.column(col, width=150)            # Set column width

table.place(x=10, y=200, width=760, height=280)  # Position the table
table.bind('<Double-Button-1>', getdata)         # Bind double-click event to fetch row

# Load existing data from DB into table
refresh_table()

# Start the Tkinter event loop
root.mainloop()