import sys
inp = next(sys.stdin).strip()
r, n = [int(i) for i in inp.split(" ")]
cache = [False] * (r + 1)
for line in sys.stdin:
    line = int(line)
    cache[line] = True

if all(cache[1:]):
    print("too late")
else:
    for k, v in enumerate(cache):
        if k == 0:
            continue
        if not v:
            print(k)
            break

