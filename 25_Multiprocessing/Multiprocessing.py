"""
Multiprocessing:-  Multiprocessing means running multiple processes at the same time, where 
    each process has its own memory space and runs independently on different CPU cores.
    No GIL problem; True parallel execution

What is a Process? = A full program; With its own memory; Running independently
    
Ex:-  Think of your computer like a house with 4 rooms (4 CPU cores).
    If you assign one worker(process) per room, they can all work at the same time without disturbing each other.

They run IN PARALLEL; They have SEPARATE memory; They are independent

When to Use Multiprocessing? (Very Important)

Use Multiprocessing for:   🧮 Heavy calculations; 🖼 Image processing; 📊 Data analysis; 🤖 Machine Learning;
    🔢 Complex loops

Do NOT use Multiprocessing for:  📁 File reading/writing; 🌐 Network requests; 🗄 Database access;
    These are I/O tasks where threads are better due to lower overhead.

Multiprocessing Functionalities:-
    multiprocessing.Process(target=Function_name):- Creates a new process and assigns a function to run.
    .start():- Starts execution of the process.
    .join():- Makes the main program wait until the process completes.
    .is_alive():- Checks if the process is still running.
    .name:- Returns the name of the process.

    
      CPU Core 1        CPU Core 2        CPU Core 3
   ┌────────────┐    ┌────────────┐    ┌────────────┐
   │ Process 1  │    │ Process 2  │    │ Process 3  │
   │ Own Memory │    │ Own Memory │    │ Own Memory │
   └────────────┘    └────────────┘    └────────────┘
"""

from multiprocessing import Process
import time

# Function for Process 1
def fun1():
    print("Process 1 start")
    time.sleep(3)   # Pause for 3 seconds (simulating a long task)
    print("Process 1 Finished")

# Function for Process 2
def fun2():
    print("Process 2 start")
    time.sleep(2)   # Pause for 2 seconds (simulating a long task)
    print("Process 2 Finished")

# This part runs only when the file is executed directly, and prevents multiprocessing from restarting the 
# program again.
if __name__ == "__main__":
    # Create two separate processes
    p1 = Process(target=fun1)   # Process 1 will run fun1()
    p2 = Process(target=fun2)   # Process 2 will run fun2()

    # Start both processes (run at the same time)
    p1.start()
    p2.start()

    # Wait until both processes finish their tasks
    p1.join()
    p2.join()

    # After both processes are done
    print("Both processes completed (Main process ends)")
# OP:
# Process 1 start
# Process 2 start
# Process 2 Finished
# Process 1 Finished
# Both processes completed (Main process ends)