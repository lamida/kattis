import sys
name = next(sys.stdin).strip()
name = [i for i in name]
trim = 0
for i in range(len(name)):
    j = i+1
    while j < len(name):
        while name[j-1] == name[j] and j < len(name)-1:
            name.pop(j)
        j+=1
print("".join(name).strip())
