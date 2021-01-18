import sys

inn = sys.stdin

ts = int(next(inn))
ss = []
while ts > 0:
    ss.append(next(inn).strip())
    ts -= 1
for line in inn:
    [a, b] = [int(i)-1 for i in line.split(" ")]
    ss[a] = "".join([ss[a], ss[b]])
    ss[b] = ""
print("".join(ss))