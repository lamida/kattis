import sys

inn = sys.stdin
next(inn)
idx = 0 
while idx != -1:
    idx = int(next(inn, -1))
    ss = set()
    for i in range(idx):
        ss.add(next(inn).strip())
    if (len(ss) != 0):
        print(len(ss))
