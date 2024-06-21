import time

def main():
    start = time.time()
    do_something()
    end = time.time()

    print(end - start)
    print(int(end - start))

def do_something():
    for a in range(50000000):
        b = a*a


main()
