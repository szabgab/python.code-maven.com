
def hello(name):
    print(f"Hello {name}")

if __name__ == "__main__":
    hello("Python")
    print(hello)

    greet = hello
    greet("Rust")
    print(greet)

