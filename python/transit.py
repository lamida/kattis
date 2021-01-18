import sys

inn = sys.stdin

(s, t, n) = (int(i) for i in next(inn).strip().split(" "))
dds = [int(i) for i in next(inn).strip().split(" ")]
bbs = [int(i) for i in next(inn).strip().split(" ")]
intervals = [int(i) for i in next(inn).strip().split(" ")]

duration = 0
for i in range(len(bbs)):
    if i == 0:
        duration += max(dds[i], intervals[i]) + bbs[i]
    else:
        duration += max((duration + dds[i]) % duration, (duration + intervals[i]) % duration) + bbs[i]
duration += dds[-1]
print("yes" if duration <= t else "no")
