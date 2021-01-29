import sys
inn = next(sys.stdin).strip()

out = [""] * (len(inn))
j = 0
i = 0
while i < len(inn):
    c = inn[i]
    if c == "<":
        j-=1
    else:
        out[j] = c
        j+=1
    i+=1
print("".join(out[:j]))
