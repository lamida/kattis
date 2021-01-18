import sys

inn = sys.stdin
next(inn)
inn = next(inn)
inn = [int(i) for i in inn.split(" ")]

cache = {}

for i,v in enumerate(inn):
    if cache.get(v) is None:
        cache[v] = i
    else:
        cache[v] = -1
mmax = -1 
idx = -1
for k,v in cache.items():
    if k > mmax and v != -1:
        mmax = k 
        idx = v
if idx == -1:
    print("none")
else:
    print(idx + 3)


