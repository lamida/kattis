import sys

inn = sys.stdin

for line in inn:
    line = line.strip()
    (r, s) = (int(i) for i in line.split(" "))
    print(2 * s - r)
