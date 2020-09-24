import sys
inn = sys.stdin
next(inn)
cache = [False] * 366
for line in inn:
    line = line.strip()
    s, t = [int(i) for i in line.split(" ")]
    for i in range(s, t+1):
        cache[i] = True
print(len([k for k in cache if k is True]))
