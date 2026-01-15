"""
Daemon Thread Concept

Normal thread = important task
   - Python waits until it finishes.

Daemon thread = background helper
   - Python does NOT wait for it.
   - It stops automatically when all normal threads finish.

Example:
- Normal thread works for 5 seconds
- Daemon thread keeps printing every 2 seconds
- When normal thread ends → daemon thread is automatically killed
"""

import threading
import time

# -------------------------------
# Background helper thread (Daemon)
# -------------------------------
def deamon_task():
    while True:
        print("Background working....")
        time.sleep(2)       # Sleep so the output slows down


# -------------------------------
# Main important task (Normal thread)
# -------------------------------
def normal_task():
    print("Normal Thread started...")
    time.sleep(5)          # Simulates some real work
    print("Normal Thread finished")


# ------------------------------------------------
# Creating a daemon thread
# daemon=True   --> marks it as a background helper
# ------------------------------------------------
deamon_thread = threading.Thread(target=deamon_task, daemon=True)

# Normal thread (default daemon=False)
normal_thread = threading.Thread(target=normal_task)

# Start both threads
deamon_thread.start()
normal_thread.start()

# Main thread waits ONLY for normal thread
normal_thread.join()

print("Main thread finished → Daemon thread stops automatically")
# OP:
# Background working....
# Normal Thread started...
# Background working....
# Background working....
# Normal Thread finished
# Main thread finished → Daemon thread stops automatically