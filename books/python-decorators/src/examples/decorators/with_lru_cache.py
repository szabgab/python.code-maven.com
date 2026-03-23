import functools

@functools.lru_cache()
def compute(x, y):
    print(f"Called with {x} and {y}")
    # some long computation here
    return x+y

if __name__ == "__main__":
    print(compute(2, 3))
    print(compute(3, 4))
    print(compute(2, 3))

