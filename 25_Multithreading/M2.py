# Thread with sleep() (Easy)
# Create a thread that prints “Hello” every 1 second, three times.
# Goal: Understand thread delay + concurrency.
import time
import threading

def fun():
    for i in range(3):
        print("Hello")
        time.sleep(1)

t1 = threading.Thread(target=fun)

t1.start()

t1.join()
print("Main thread finished")
# OP:
# Hello
# Hello
# Hello
# Main thread finished