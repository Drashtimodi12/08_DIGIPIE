# Simulate a server handling requests one by one (blocking).
# Requirements:
# Make a function handle_request()
# Takes a request → sleeps 2 seconds
# Process 5 requests sequentially
# Print how much time it takes

import time

def handle_request(request_number):
    print(f"Processing request {request_number}...")
    time.sleep(2)
    print(f"Request {request_number} completed.")

start = time.perf_counter()
for i in range(1, 5):
    handle_request(i)

end = time.perf_counter()
print(f"Total server time: {end - start:.2f} seconds")
# OP:
# Processing request 1...
# Request 1 completed.
# Processing request 2...
# Request 2 completed.
# Processing request 3...
# Request 3 completed.
# Processing request 4...
# Request 4 completed.
# Total server time: 8.00 seconds