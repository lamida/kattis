# This is still time limit exceeded
import sys

c = int(next(sys.stdin))

txt = "A"
for i in range(c):
    new_txt = ""
    for c in txt:
        if c == "A":
            new_txt += "B"
        else:
            new_txt += "BA"
    txt = new_txt
ct = [0, 0]
for c in txt:
    if c == "A":
        ct[0] += 1
    else:
        ct[1] += 1
print(ct[0], ct[1])