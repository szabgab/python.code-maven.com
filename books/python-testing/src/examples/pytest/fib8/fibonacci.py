def fib(n):
    var_type = type(n).__name__
    if var_type != 'int':
        raise ValueError(f'Invalid value type of "{n}" is "{var_type}"')
    if n < 1:
        raise ValueError(f'Invalid parameter {n} is negative')
    a, b = 1, 1
    for _ in range(1, n):
        a, b = b, a+b
    return a

