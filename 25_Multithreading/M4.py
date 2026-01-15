# Use join()
# Create 3 threads that each print a message after sleeping for a random time (1–5 seconds).
# The main program should wait until all threads are done.
# Goal: Learn join() properly.

import threading
import time
import random

def task1():
    delay = random.randint(1, 5)
    time.sleep(delay)
    print(f"Task 1 completed after {delay} seconds")

def task2():
    delay = random.randint(1, 5)
    time.sleep(delay)
    print(f"Task 2 completed after {delay} seconds")

def task3():
    delay = random.randint(1, 5)
    time.sleep(delay)
    print(f"Task 3 completed after {delay} seconds")


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)

t1.start()
t2.start()
t3.start()

# Main thread waits for all to finish
t1.join()
t2.join()
t3.join()

print("All threads finished! (Main thread ends)")
# OP:
# Task 1 completed after 1 seconds
# Task 2 completed after 1 seconds
# Task 3 completed after 4 seconds
# All threads finished! (Main thread ends)