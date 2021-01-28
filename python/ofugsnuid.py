import sys
next(sys.stdin)
l = []
for line in sys.stdin:
    x = int(line)
    l += [x]
for i in range(len(l) -1, -1, -1):
    print(l[i])
