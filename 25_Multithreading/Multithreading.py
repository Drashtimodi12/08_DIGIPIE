"""
What is Multithreading? :-     It running many tasks at the same time inside ONE program.

Ex:- Imagine your brain doing multiple small tasks at the same time.
    You are:-   Listening to music, Downloading a file, Writing notes 

Your brain = the process
Each task = a thread

What is a Thread?:-     A small part of a program, That can run separately, Inside the same program

A program can have:     1 thread → single task;     many threads → multiple tasks at once

Threading = Using multiple threads inside one program
        Python gives you a module called threading to create and manage threads.

When Should You Use Multithreading?
    Use multithreading when your program is doing I/O tasks, like:
    Downloading files, Reading/writing files, Database queries, API calls, Waiting for network, Uploading files
    These tasks spend time waiting, so while one waits, another thread can work.

When NOT to Use Multithreading?:-   Multithreading is NOT useful for heavy calculations, like:
    Big loops, Millions of math operations, Image processing, Machine learning calculations
    Because of something called GIL.
    
What is GIL(Global Interpreter Lock)?
    Think of it like:   A bathroom 🛁 with only ONE key
    Only ONE person can use the bathroom at a time
    Even if 10 people (threads) are waiting

In Python:  Even if you create many threads, Only ONE thread can execute Python code at a time.

# So multithreading is bad for CPU-heavy tasks.

            ONE PROGRAM
          (One memory area)
                 |
      ------------------------
      |          |           |
   Thread 1   Thread 2    Thread 3
      |          |           |
   (Run)       (Run)       (Run)


Threading Functionalities:-
    threading.Thread(target=Function_name):- Creates a new thread and assigns a function for it to execute.
    start():- Begins the execution of the thread’s assigned function.
    join():- Stops the main program until the thread has finished running.
    is_alive():- Checks whether the thread is still running or has completed.
    current_thread():- Returns the thread that is currently executing the code.
    daemon = True:- Marks the thread as a background thread that ends when the main program ends.

All threads run inside one single process. Threads share memory.    
Because of GIL → only one thread runs Python code at a time
"""

import threading
import time

# Function that represents Task 1
def fun1():
    print("Function 1 start")
    time.sleep(3)   # Simulating a 3-second time-taking task
    print("Function 1 Finished")

# Function that represents Task 2
def fun2():
    print("Function 2 start")
    time.sleep(2)   # Simulating a 2-second time-taking task
    print("Function 2 Finished")

# Creating two threads and assigning tasks to them
t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)

# Starting both threads (they run at the same time)
t1.start()
t2.start()

# Wait for both threads to finish before ending the main program
t1.join()
t2.join()

print("Both tasks completed (Main thread ends)")
# OP:
# Function 1 start
# Function 2 start
# Function 2 Finished
# Function 1 Finished
# Both tasks completed (Main thread ends)