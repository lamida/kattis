import sys
res = 0
i = 0
for line in sys.stdin:
    n = int(line.strip())
    i+=1
    if i == 1:
        continue
    print(n, "is even" if n % 2 == 0 else "is odd") 
    

