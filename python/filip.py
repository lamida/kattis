import sys

inn = sys.stdin

(a, b) = (int("".join(list(reversed(x)))) for x in next(inn).strip().split(" "))
print(max(a, b))
