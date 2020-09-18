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
print(cache)
mmax = -1
for k,v in cache.items():
    if v > mmax:
        mmax = k 
if mmax == -1:
    print("none")
else:
    print(cache[mmax] + 1)


