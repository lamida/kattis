# Still wrong answer
import sys
next(sys.stdin)

l = []
for line in sys.stdin:
    l += [ord(line.strip()[0])]

o = None
i = 0
while i < len(l) - 1:
    a = l[i]
    b = l[i+1]
    if o is None:
        if a < b:
            o = "INCREASING"
        if a > b:
            o = "DECREASING"
    else:
        if a < b and o != "INCREASING":
            o = "NEITHER"
            break
        if a > b and o != "DECREASING":
            o = "NEITHER"
            break
    i+=1
print("NEITHER" if o is None else o)
        

