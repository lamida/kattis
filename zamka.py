import sys
inn = sys.stdin
ii = [0] * 3
i = 0
for line in inn:
    line = line.strip()
    ii[i] = int(line)
    i+=1

(l, d, x) = ii
for i in range (l, d + 1):
    s = 0
    for c in str(i):
        s += int(c)
    if s == x:
        print(i)
        break
for i in range (d, l - 1, -1):
    s = 0
    for c in str(i):
        s += int(c)
    if s == x:
        print(i)
        break
