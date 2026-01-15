"""
Why do we need is_alive()?
    Imagine you start a thread that does some task (like downloading, processing, sleeping, etc.)
    While the thread is doing work, your main program can check:
thread.is_alive()
    If the thread is still working → it returns True
    If the thread has completed → it returns False
"""



# Check is_alive()
# Start a thread that sleeps 3 seconds.
# While it is running, keep checking:
# Thread Alive: True
# When it finishes, print:
# Thread Alive: False

import threading
import time

def fun():
    time.sleep(3)

t = threading.Thread(target=fun)
t.start()

while t.is_alive():
    print("Thread Alive: True")
    time.sleep(0.5)
print("Thread Alive: False")
# OP:
# Thread Alive: True
# Thread Alive: True
# Thread Alive: True
# Thread Alive: True
# Thread Alive: True
# Thread Alive: True
# Thread Alive: False