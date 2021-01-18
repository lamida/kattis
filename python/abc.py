import sys

inn = sys.stdin

nums = [int(i) for i in next(inn).split(" ")]
abc = next(inn)

res = 3 * [0]
mmax = max(nums)
mmin = min(nums)
for i in range(3):
    key = abc[i]
    if key == 'A':
        res[i] = mmin
    elif key == 'B':
        for x in nums:
            if x != mmax and x != mmin:
                res[i] = x
    else:
        res[i] = mmax
print(" ".join([str(i) for i in res]))
    