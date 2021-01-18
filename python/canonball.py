import sys
from math import sin, cos, pi

inn = sys.stdin

next(inn)
for line in inn:
    line = line.strip()
    (v0, teta, x1, h1, h2) = (float(i) for i in line.split(" "))
    t_cross = x1/(v0 * cos(teta*pi/180))
    y_cross = v0 * t_cross * sin(teta*pi/180) - 0.5*9.81*t_cross**2
    print("Safe" if y_cross - h1 >= 1 and h2 - y_cross >= 1 else "Not Safe")
