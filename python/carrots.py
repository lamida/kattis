import sys
res = 0
for line in sys.stdin:
    (n, hp) = [int(i.strip()) for i in line.split(" ")]
    res = hp
    break
print(res)
