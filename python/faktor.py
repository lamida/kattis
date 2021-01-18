import sys

(a, i) = (int(i) for i in next(sys.stdin).strip().split(" "))
print(a*(i-1) + 1)
