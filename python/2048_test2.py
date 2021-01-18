list = [2, 2, 2, 2]

for i in range(3, 0, -1):
    j = i
    while list[j] == 0 and j > 0:
        if list[j - 1] != 0:
            list[j - 1], list[j] = list[j], list[j - 1]
        j-=1
for i in range(3, 0, -1):
    j = i - 1
    if list[i] == list[j]:
        list[i], list[j] = list[i] + list[j], 0
for i in range(3, 0, -1):
    j = i
    while list[j] == 0 and j > 0:
        if list[j - 1] != 0:
            list[j - 1], list[j] = list[j], list[j - 1]
        j-=1
print(list)
