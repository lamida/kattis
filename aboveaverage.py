import sys
next(sys.stdin)

for line in sys.stdin:
    all = [int(i) for i in line.split(" ")]
    n = all[0]
    grades = all[1:]
    average = sum(grades)/n
    count = 0
    for i in grades:
        if i > average:
            count+=1
    print("{:.3f}%".format(100 * count / n))