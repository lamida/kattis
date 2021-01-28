import sys
# skip first line
next(sys.stdin)
c = 1
for line in sys.stdin:
    number, source, target = line.strip().split(" ")
    print(f"Case #{c}: fooo")
    c += 1