import sys

inn = sys.stdin
next(inn)

for line in inn:
    line = line.strip()
    (n, x, y, w, h) = line.split(" ")
