# Run two functions at the same time
# Write two functions:
# Function A: prints "Downloading..." 5 times
# Function B: prints "Processing..." 5 times
# Run them using two threads.

import threading
import time

def fun1():
    for i in range(5):
        print("Downloading threads...")
        time.sleep(4)

def fun2():
    for i in range(5):
        print("Processing threads...")
        time.sleep(5)


t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Both tasks completed (Main thread ends)")
# OP:
# Downloading threads...
# Processing threads...
# Downloading threads...
# Processing threads...
# Downloading threads...
# Processing threads...
# Downloading threads...
# Processing threads...
# Downloading threads...
# Processing threads...
# Both tasks completed (Main thread ends)