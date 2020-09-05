import sys
res = 0
i = 0
for line in sys.stdin:
    i+=1
    if i == 1:
        continue
    res = len(list(filter(lambda x: x<0, [int(i) for i in line.strip().split(" ")])))
print(res)
    

