import os

def add():
    a = os.environ.get("INPUT_A")
    b = os.environ.get("INPUT_B")
    if a is None:
        raise Exception("missing INPUT_A")
    if b is None:
        raise Exception("missing INPUT_B")

    a = int(a)
    b = int(b)
    return a + b
