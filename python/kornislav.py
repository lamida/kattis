import sys
inn = [int(i) for i in next(sys.stdin).split(" ")]
inn.sort()
print(inn[0] * inn[2])
