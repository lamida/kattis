import sys
e, f, c = [int(i) for i in (next(sys.stdin).split(" "))]

soda = 0
e = e + f
prev_rem = 0
while e != 0:
    e += prev_rem
    buy = e // c
    rem = e % c
    soda += buy
    e = buy
    prev_rem = rem
print(soda)