import sys

inn = sys.stdin
next(inn)

df = {}
def traverse(cc, n):
    # if df.get(n) is not None:
    #     return df[n]
    if cc[n][0] == "favourably":
        df[n] = 1
        return 1
    elif cc[n][0] == "catastrophically":
        df[n] = 0
        return 0
    else:
        count = 0
        for i in cc[n]:
            count += traverse(cc, int(i))
        # df[n] = count
        return count

cache = {}
c = 0
for line in inn:
    elems = line.strip().split(" ")
    if len(elems) == 1:
        if len(cache) == 0:
            continue
        c = traverse(cache, 1)
        print(c)
        cache = {}
    elif len(elems) == 4:
        cache[int(elems[0])] = elems[1:]
    else:
        cache[int(elems[0])] = [elems[1]]
c = traverse(cache, 1)
print(c)
