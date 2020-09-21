import sys

inn = sys.stdin
x = int(next(inn))
n = int(next(inn))
quota = x 
while n > 0:
    quota += x
    p = int(next(inn))
    quota -= p
    n -= 1
print(quota)