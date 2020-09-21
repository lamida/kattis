import sys

inn = sys.stdin

for line in inn:
    (a, b) = (int(i) for i in line.split(" "))
    print(abs(a-b))
