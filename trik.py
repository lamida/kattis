import sys

inn = sys.stdin
moves = next(inn).strip()

cups = [True, False, False]

for c in moves:
    if c == "A":
        cups[0], cups[1] = cups[1], cups[0]
    elif c == "B":
        cups[1], cups[2] = cups[2], cups[1]
    elif c == "C":
        cups[0], cups[2] = cups[2], cups[0]
for i in range(len(cups)):
    if cups[i]:
        print(i + 1)
