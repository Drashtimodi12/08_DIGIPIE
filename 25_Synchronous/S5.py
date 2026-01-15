# Read 3 different text files in order and measure how long each takes.
# Requirements:
# Create files: file1.txt, file2.txt, file3.txt
# Put different text in each file
# Read them sequentially (one after another)
# Measure time taken for each
# Print total time

import time

files = ["S51.txt", "S52.txt", "S53.txt"]

start = time.perf_counter()

for file in files:
    file_start = time.perf_counter()

    with open(file, "r") as f:
        data = f.read()
        print(data)
        time.sleep(2)  # simulate slow read

    file_end = time.perf_counter()
    print(f"{file} read in {file_end - file_start:.2f} seconds")

end = time.perf_counter()

print(f"Total time: {end - start:.2f} seconds")
# OP:
# Hello
# S51.txt read in 2.01 seconds
# Learner
# S52.txt read in 2.03 seconds
# I am Drashti...
# S53.txt read in 2.04 seconds
# Total time: 6.08 seconds
