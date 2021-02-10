import sys
next(sys.stdin)

ll = []
for line in sys.stdin:
    ll += [line.strip()]

ans = ll[1:]

score = 0
for i in range(len(ans)):
    if ll[i] == ans[i]:
        score +=1
print(score)