import sys

inn = sys.stdin
ss = next(inn)
[jack, jill] = [int(i) for i in ss.split(" ")]
while jack != 0 and jill !=0:
    cache = {}
    while jack > 0:
        x = next(inn)
        cache[int(x)] = 1
        jack -=1
    count = 0
    while jill > 0:
        x = next(inn)
        if cache.get(int(x)) is not None:
            count+=1
        jill -=1
    print(count)
    [jack, jill] = [int(i) for i in next(inn).split(" ")]



