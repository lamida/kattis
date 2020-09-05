import sys
inn = sys.stdin
next(inn)
res = 0
for line in inn:
    line = line.strip()
    n = int(line[:len(line)-1])
    pw = int(line[-1])
    res += pow(n, pw)
print(res)

