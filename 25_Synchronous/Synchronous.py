"""
Definition:- one task happens at a time, in order. You must wait for the current task to finish before 
        the next one starts.

Ex: standing in a line at a ticket counter — the next person is served only after the previous person finishes.

How it works internally:
    If Task 1 takes 5 seconds → Python waits for 5 seconds.
    Only then does Task 2 start.
    Other tasks cannot run in parallel.
    If one task is slow, the entire program slows down.

Good for:- Simple tasks, Predictable flow, Code readability
Not good for:- Slow operations (network, downloading), Apps needing high performance, Handling many users (web servers)

Task 1 -----> Task 2 -----> Task 3 -----> Task 4
(Waits)       (Waits)       (Waits)       (Waits)

Where Synchronous Is Commonly Used?
    CPU-heavy calculations
    Simple scripts
    File handling (reading/writing files)
    CLI (command-line) programs
    Backend functions that don’t involve long I/O waits

"""

import time   # time.sleep() is used to simulate a time-consuming task

def fun1():
    time.sleep(2)          # Simulating a delay of 2 seconds
    print("Task 1 Perform")

def fun2():
    time.sleep(2)          # Simulating a delay of 2 seconds
    print("Task 2 Perform")

def main():
    print("Start to perform task...")
    fun1()  # First complete Task 1
    fun2()  # After Task 1 finishes, start Task 2
    print("End all task...")

# Running the synchronous program
main()  # Total time = 2 sec + 2 sec = 4 seconds
# OP:
# Start to perform task...
# Task 1 Perform
# Task 2 Perform
# End all task...