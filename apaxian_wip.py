
name = "rrobert"

for i in range(len(name) - 1):
    j = i + 1
    while name[i] == name[j] and j < len(name):
        name[i], name[j] = name[j], name[i]
