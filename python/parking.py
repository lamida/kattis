import sys

i = 0
for line in sys.stdin:
    if i == 0: 
        i+=1
        continue
    if i%2 == 0:
        spots = [int(i) for i in line.split(" ")]
        print(2 * (max(spots) - min(spots)))
        i+=1
    else:
        i+=1
        continue

    
