"""
flush Parameter:-  flush=True tells Python to force print the output immediately.
    Normally, Python waits and prints when buffer is full.

flush=True prints instantly → useful for:
    Live progress bars
    Loading animations
    Real-time logs
"""

import time

for i in range(1, 6):
    print(i, end = " ", flush=True)
    time.sleep(1)       # Numbers change every 1 second in the same line
    # Without flush, Python may delay printing
# OP: 1 2 3 4 5 