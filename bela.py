import sys

inn = sys.stdin

weight = {"A": (11, 11), "K": (4,4), "Q": (3, 3), "J": (20, 2), "T": (10, 10), "9": (14, 0), "8": (0, 0), "7": (0, 0)}

(hand, dom) = next(inn).strip().split(" ")
hand = int(hand)

ssum = 0
for line in inn:
    line = line.strip()
    (num, suite) = line[0], line[1]
    is_dom = suite == dom
    val = weight[num]
    ssum += (val[0] if is_dom else val[1])
print(ssum)

