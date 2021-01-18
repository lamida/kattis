import sys

c = 1
for line in sys.stdin:
    inp = [int(i) for i in line.split(" ")][1:]
    mmin = min(inp)
    mmax = max(inp)
    rrange = mmax - mmin
    print(f"Case {c}:", mmin, mmax, rrange)
    c+=1

    