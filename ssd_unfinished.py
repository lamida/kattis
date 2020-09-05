import sys

inn = sys.stdin
next(inn)

for line in inn:
    line = line.strip()
    (k, b, n) = (i for i in line.split(" "))
    ssum = 0
    pw = 0
    for i in range(len(n) - 1, -1, -1):
        print(n[i], "times", b, "pow", pw)
        ssum += int(n[i]) * (int(b)**pw)
        pw +=1
    print(ssum)
    fin = 0
    for i in str(ssum):
        fin += (int(i) ** 2)
    print(k, fin)


