import sys
next(sys.stdin)

idx = 1
for line in sys.stdin:
    (k, n) = (int(i) for i in line.split(" "))
    s1 = 0
    s2 = 0
    s3 = 0
    for i in range(1, n + 1):
        s1 += i
    for i in range(1, n*2 + 1, 2):
        s2 += i
    for i in range(0, n*2 + 1, 2):
        s3 += i
    print(idx, s1, s2, s3)
    idx += 1
