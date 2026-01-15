# The grid method in Tkinter is used to organize widgets in a table-like structure in the parent widget. 
# It allows you to specify the row and column where you want to place each widget. 
# This method provides a flexible way to control the layout of widgets in a window.

from tkinter import *   # Import all classes and functions from the tkinter module

# Create the main application window
root = Tk()
root.geometry("500x500")        # Set the window size to 500x500 pixels


# Create and place labels using the grid method
# The grid method positions the widget in a grid layout based on row and column arguments
l1 = Label(text="Username").grid(row=1,column=1)
l2 = Label(text="Email").grid(row=2,column=1)
l3 = Label(text="Password").grid(row=3,column=1)

# Create entry widgets for user input and place them using the grid method
e1 = Entry().grid(row=1,column=2)
e2 = Entry().grid(row=2,column=2)
e3 = Entry().grid(row=3,column=2)

# Create and place a button using the grid method
Button(text="submit").grid(row=4,column=2)

# Start the Tkinter event loop
root.mainloop()