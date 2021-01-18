import sys
from math import pi, sin, ceil
valid = [1, 1, 2, 2, 2, 8]
for line in sys.stdin:
    (h,v) = [int(i.strip()) for i in line.split(" ")]
    res = h / sin(v * pi/180)
    print(ceil(res))

