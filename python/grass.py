import sys

inn = sys.stdin

price = float(next(inn).strip())
next(inn)

total = 0
for line in inn:
    (w, l) = (float(i) for i in line.strip().split(" "))
    total += (w * l)

t = total * price
print("%.7f" % t)
