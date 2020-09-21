import sys
from math import sqrt

inn = int(next(sys.stdin))

def process(n):
    print(n)
    if n == 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            print("mod",i)
            return 1 + process(n//i)
print(process(inn))