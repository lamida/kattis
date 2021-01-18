import sys
valid = [1, 1, 2, 2, 2, 8]
for line in sys.stdin:
    inn = [int(i.strip()) for i in line.split(" ")]
    for i in range(len(inn)):
        valid[i] -= inn[i]
print(" ".join([str(i) for i in valid]))
