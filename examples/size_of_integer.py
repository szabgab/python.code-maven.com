import sys


print(f"   i size len                                               2**i")
for i in range(0, 261, 10):
    number = 2**i
    print(f"{i:4} {sys.getsizeof(number):4} {len(str(number)):3} {number:100}")
