import sys
name = next(sys.stdin).strip()
result = ""
i = 0
while i < len(name):
    j = i + 1
    if j < len(name) and name[i] != name[j]:
        result += name[i]
        i+=1
        j+=1
    else:
        while i < len(name) and j < len(name) and name[i] == name[j]:
            i+=1
            j+=1
        result += name[i]
        i += 1
print(result)
