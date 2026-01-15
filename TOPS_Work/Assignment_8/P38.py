# 38.	Write a Python program to create a basic GUI window using Tkinter.

from tkinter import *  # Import all classes and functions from the tkinter module

# Create the main application window
root = Tk()
root.title("BASIC GUI WINDOW.")     # Set the window title
root.geometry("500x500")        # Set the window size to 500x500 pixels


# Create a label widget and place it in the window
l1 = Label(root, text="Hello Tkinter!", font=('Arial', 20)).pack(pady=20)   # Use pack geometry manager to center the label with padding

# Create a button widget and place it in the window
button = Button(root, text="Click Me", font=('Arial', 20)).pack(pady=10)

# Start the Tkinter event loop
root.mainloop()