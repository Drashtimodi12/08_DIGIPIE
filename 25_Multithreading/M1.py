# Print numbers using two threads (Very Easy)
# Create two threads:
# Thread-1 prints numbers 1 to 5
# Thread-2 prints numbers 6 to 10
# Goal: Understand thread creation and starting.

import threading        # threading module helps us create and manage threads
import time

def fun1():
    
    for i in range(1, 6):
        start_time = time.perf_counter()
        print(i, end=" ")
        time.sleep(4)
        end_time = time.perf_counter()
    print("Difference func1: ", end_time - start_time)
    



def fun2():
    
    for i in range(6, 11):
        start_time = time.perf_counter()
        print(i, end=" ")
        time.sleep(2)
        end_time = time.perf_counter()
    print("Difference func1: ", end_time - start_time)


# threading.Thread() → creates a new thread
# target=function_name → tells thread what function to run
t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)

# start() → begins the execution of thread
# Now both threads will run at the SAME TIME (concurrent execution)
t1.start()
t2.start()

# join() → main thread waits until the thread completes
# If we don’t use join(), main thread will finish early.
t1.join()
t2.join()

print("Both tasks completed (Main thread ends)")

# OP:
# 1 6 7 2 8 9 3 10 Difference func1:  2.0001941000227816
# 4 5 Difference func1:  4.000213799998164
# Both tasks completed (Main thread ends)


print("\n====================================\n")







import threading
import time


def print_one_to_six():
    start = time.time()        # Function start time
    for i in range(1, 7):
        print(f"Function 1: {i}")
        time.sleep(4)
    end = time.time()          # Function end time
    print(f"Function 1 total time: {end - start:.2f} seconds")



def print_six_to_eleven():
    start = time.time()        # Function start time
    for i in range(6, 12):
        print(f"Function 2: {i}")
        time.sleep(2)
    end = time.time()          # Function end time
    print(f"Function 2 total time: {end - start:.2f} seconds")



t1 = threading.Thread(target=print_one_to_six)
t2 = threading.Thread(target=print_six_to_eleven)


t1.start()
t2.start()


t1.join()
t2.join()


print("All threads Done!")

# OP:
# Function 1: 1
# Function 2: 6
# Function 2: 7
# Function 1: 2
# Function 2: 8
# Function 2: 9
# Function 1: 3
# Function 2: 10
# Function 2: 11
# Function 1: 4
# Function 2 total time: 12.02 seconds
# Function 1: 5
# Function 1: 6
# Function 1 total time: 24.01 seconds
# All threads Done!