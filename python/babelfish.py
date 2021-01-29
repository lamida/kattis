import sys
d = {}
translate = False
for line in sys.stdin:
    line = line.strip()
    if line == "":
        translate=True
        continue
    elif translate:
        tr = d.get(line)
        if tr is None:
            print("eh")
        else:
            print(tr)
    else:
        token = line.split(" ")
        if len(token) == 2:
            k, v = token
            d[v] = k