import sys

inn = sys.stdin
next(inn)
for line in inn:
    n = int(line.strip())
    res = 1
    for i in range(1, n + 1):
        res *= i
        res %= 10
    print(res)

