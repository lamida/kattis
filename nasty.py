import sys

inn = sys.stdin
next(inn)

for line in inn:
    line = line.strip()
    (r, e, c) = (int(i) for i in line.split(" "))
    rev_ad = e - c
    if rev_ad > r:
        print("advertise")
    if rev_ad < r:
        print("do not advertise")
    if rev_ad == r:
        print("does not matter")
