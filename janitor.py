import sys
from math import sqrt
inn = sys.stdin

[a, b, c, d] = [int(i) for i in next(inn).split(" ")]
s = (a + b + c + d) / 2;
print(sqrt((s-a) * (s-b) * (s-c) *(s-d)))