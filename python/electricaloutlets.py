import sys
next(sys.stdin)

for line in sys.stdin:
    apps = [int(i) for i in line.split()][1:]
    print(sum(apps) - (len(apps) - 1))