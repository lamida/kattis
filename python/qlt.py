import sys

inn = sys.stdin

next(inn)
res = 0
for line in inn:
    line = line.strip()
    (q, y) = (float(i) for i in line.split(" "))
    res += q * y 
print("%.3f" % res)

