# Simulate calling 5 different APIs in parallel instead of sequentially.
# Task Description:
# Create a function fetch_api(n) that:
# prints: "Calling API n..."
# waits 2 seconds
# prints: "API n response received!"
# Then run 5 API calls together using asyncio.gather().

import time
import asyncio

async def API(n):
    print(f"Calling API {n}...")
    await asyncio.sleep(2)
    print(f"API {n} response received!")
    
async def main():
    start = time.time()
    await asyncio.gather(API(1), API(2), API(3), API(4), API(5))
    end = time.time()
    print(f"All API calling time is {end - start:.2f} seconds.\n")

asyncio.run(main())
# OP:
# Calling API 1...
# Calling API 2...
# Calling API 3...
# Calling API 4...
# Calling API 5...
# API 1 response received!
# API 2 response received!
# API 3 response received!
# API 4 response received!
# API 5 response received!
# All API calling time is 2.02 seconds.