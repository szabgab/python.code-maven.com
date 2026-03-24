import time

def wrap(func):
    def new_function():
        print(f"start new '{func.__name__}'")
        start = time.time()
        func()
        end = time.time()
        print(f"end new '{func.__name__}' {end-start}")
    return new_function

