class MyContext:
    def __enter__(self):
        print("Entering the block")
        return "Hello"
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the block")

with MyContext() as msg:
    print(msg)