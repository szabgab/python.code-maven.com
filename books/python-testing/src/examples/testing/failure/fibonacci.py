def fib(n):
    """
    Fibonacci sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

    >>> fib(1)
    0

    >>> fib(7)
    8

    >>> fib(10)
    34

    >>> fib(42)
    165580141
    """
    fibs = [0, 1]
    for _ in range(n-2):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[-1]

