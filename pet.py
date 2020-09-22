import sys

inn = sys.stdin

mmax = -1
idx = 1
current = 1
for line in inn:
    tot = sum([int(i) for i in line.split(" ")])
    if tot > mmax:
        mmax = tot
        idx = current
    current +=1
print(idx, mmax)


