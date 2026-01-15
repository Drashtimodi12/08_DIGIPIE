from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering the block")
    yield "Hello"
    print("Exiting the block")

with my_context() as msg:
    print(msg)  


      