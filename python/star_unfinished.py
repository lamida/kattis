import sys
n = int(next(sys.stdin).strip())

print(n + ":")
for i in range(2, 1 + n/2):
    pair = n % i
    print(i, pair)
    

