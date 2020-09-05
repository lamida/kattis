import sys

inn = sys.stdin

for line in inn:
    n = int(line.strip())
    last = 2
    current = 0
    for i in range(n):
        current = last + (last-1) 
        last = current
    print(current**2)

