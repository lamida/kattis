list = [2, 2, 2, 2]

for i in range(3):
    j = i
    while list[j] == 0 and j < 2:
        if list[j + 1] != 0:
            print("swap", j, j+1)
            list[j + 1], list[j] = list[j], list[j + 1]
        j+=1
for i in range(3):
    j = i + 1
    if list[i] == list[j]:
        list[i], list[j] = list[i] + list[j], 0
for i in range(3):
    j = i
    while list[j] == 0 and j < 2:
        if list[j + 1] != 0:
            print("swap", j, j+1)
            list[j + 1], list[j] = list[j], list[j + 1]
        j+=1
print(list)
