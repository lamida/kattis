import sys

inn = sys.stdin
next(inn)

for line in inn:
    [k, n] = [int(i) for i in line.split(" ")]
    ssum = 0
    for i in range(1, n+1):
        ssum += i
    ssum += n
    print(k, ssum)
