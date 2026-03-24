from function_assignment import hello

def test_assignment(check_out):
    hello("Python")
    check_out("Hello Python\n")
    assert hello.__name__ == "hello"

    greet = hello

    greet("Rust")
    check_out("Hello Rust\n")
    assert greet.__name__ == "hello"

