# The pack method in Tkinter is used to organize widgets in blocks before placing them in the parent widget. 
# It is one of the three geometry managers in Tkinter (the others being grid and place). 
# The pack method arranges widgets by placing them on top of each other (or side by side) in the order they were packed.


from tkinter import *   # Import all classes and functions from the tkinter module

# Create the main application window
root = Tk()
root.geometry("500x500")        # Set the window size to 500x500 pixels

# Create button widgets and pack them in different positions
b1 = Button(text="Add").pack(side=LEFT)
b2 = Button(text="Sub").pack(side=RIGHT)
b3 = Button(text="Mul").pack(side=TOP)
b4 = Button(text="Div").pack(side=BOTTOM)

# Start the Tkinter event loop
root.mainloop()