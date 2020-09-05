import sys
start = {}
end = {}
for line in sys.stdin:
    (x, y) = (i.strip() for i in line.split(" "))
    if start.get(x) == None:
        start[x] = []
    start[x].append((x, y))
    if end.get(y) == None:
        end[y] = []
    end[y].append((x, y))
    

print(start, end)
        
xy = []
for k in start:
    if len(start[k]) <= 1:
        xy.append(k)
for k in end:
    if len(end[k]) <= 1:
        xy.append(k)
print(" ".join(xy))
