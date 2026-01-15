# Create a text file named example.txt with some content.
# Here the program will
# open file
# read file
# close file
# then print next message
# Everything happens step-by-step → synchronous.

import time

def create_file():
    start = time.time()
    with open('S3.txt', 'w+') as f:
        f.seek(0)
        f.write("Hello Learner")
        time.sleep(3)
        f.seek(0)
        data = f.read()
        print(data)
    time.sleep(2)
    end = time.time()
    print(f"To perform task it takse {end - start:.2f} second...")

print("Starting Task...")
create_file()
print("End Task...")
# OP:
# Starting Task...
# Hello Learner
# To perform task it takse 5.00 second...
# End Task...