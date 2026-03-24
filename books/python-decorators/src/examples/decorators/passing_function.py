def call(func):
    return func(42)

def double(val):
    return 2 * val

def square(val):
    return val * val

if __name__ == "__main__":
    print(call(double))            # 84
    print(call(square))            # 1764
    print(call(lambda x: x // 2))  # 21
