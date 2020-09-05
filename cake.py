import sys

inn = sys.stdin

for line in inn:
    line = line.strip()
    (n, h, v) = (int(i) for i in line.split(" "))
    x = max(h, n - h)
    y = max(v, n - v)
    print(x * y * 4)

