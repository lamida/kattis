import sys
inn = sys.stdin
(n, m) = (int(i) for i in next(inn).strip().split(" "))
cache = [0] * (n + m + 1)
for i in range(1, m + 1):
    for j in range(1, n + 1):
        cache[i+j]+=1

mx = max(cache)

for i in range(1, len(cache)):
    if cache[i] == mx:
        print(i)
    


