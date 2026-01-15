# Check Process Status Using is_alive()
# Create a process that:
#     prints “Process working…”
#     sleeps for 3 seconds
#     prints “Process finished”
# While the process is running, the main program should print:
#     Main: Checking process...
#     Alive: True
#         After process ends:
#     Alive: False
# Goal: Learn is_alive() + process monitoring.

from multiprocessing import Process
import time

def fun():
    print("Process working...")
    time.sleep(3)
    print("Process finished.")

if __name__ == "__main__":
    p = Process(target=fun)
    p.start()

    while p.is_alive():
        print("Main: Checking process...")
        print(f"Alive: {p.is_alive()}")
        time.sleep(0.5)
        
    # Final check after process ends
    p.join()
    print(f"Alive: {p.is_alive()}")

    
    print("Process has ended.")
# OP: 
# Main: Checking process...
# Alive: True
# Process working...
# Main: Checking process...
# Alive: True
# Main: Checking process...
# Alive: True
# Main: Checking process...
# Alive: True
# Main: Checking process...
# Alive: True
# Main: Checking process...
# Alive: True
# Main: Checking process...
# Alive: True
# Process finished.
# Alive: False
# Process has ended.