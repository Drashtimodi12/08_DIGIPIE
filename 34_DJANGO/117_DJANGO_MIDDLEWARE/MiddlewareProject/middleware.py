import time   # Used to calculate time

class SimpleLogMiddleware:

    def __init__(self, get_response):
        # This runs only once when server starts
        # One-time configuration and initialization.
        self.get_response = get_response
        print("Middleware Initialized!")

    def __call__(self, request):
# Code to be executed for each request before the view (and later middleware) are called.

        # This runs for every request
        print("Request Received")

        # Start time before view executes
        start_time = time.time()

        # Pass request to view and get response
        response = self.get_response(request)

# Code to be executed for each request/response after the view is called.

        # End time after response is ready
        end_time = time.time()

        # Print total time taken
        print(f"Response Sent | Time Taken: {end_time - start_time:.2f} seconds")

        # Return response to browser
        return response


# Terminal OP:
# Welcome to Middleware!
# Middleware Initialized!
# December 16, 2025 - 11:20:52