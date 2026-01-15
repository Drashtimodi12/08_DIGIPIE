# Task 7: Exclusive Creation (x)
# Try creating a file log.txt using x mode.
# Write "Log file created" inside.
# Run the code twice to see the FileExistsError.

with open('F7.txt', 'x') as f:
    f.write("Log file Created.")