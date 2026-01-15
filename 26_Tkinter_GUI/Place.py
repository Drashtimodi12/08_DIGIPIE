# The place method in Tkinter is used to position widgets at absolute coordinates within the parent widget. 
# This method allows for more precise control over the location of widgets compared to pack and grid.

from tkinter import *   # Import all classes and functions from the tkinter module

# Create the main application window
root = Tk()
root.geometry("500x500")        # Set the window size to 500x500 pixels

# Create and place labels using the place method
# The place method positions the widget at the specified x and y coordinates
l1 = Label(text="Username").place(x=100,y=100)
l2 = Label(text="Email").place(x=100,y=150)
l3 = Label(text="Password").place(x=100,y=200)

# Create entry widgets for user input and place them using the place method
e1 = Entry().place(x=200,y=100)
e2 = Entry().place(x=200,y=150)
e3 = Entry().place(x=200,y=200)

# Create and place a button using the place method
Button(text="submit", width=15).place(x=200, y=250)  # Place the Button widget at coordinates (200, 250)

# Start the Tkinter event loop
root.mainloop()