# Wrong answer
# This should be combined with knasack
import sys
cap = int(next(sys.stdin).split(" ")[1])
cash = []
time = []
for line in sys.stdin:
    c, t = [int(i) for i in line.split(" ")]
    cash += [c]
    time += [t]

sum = 0
for i in range(cap):
    cc = []
    for j in range(len(time)):
        if time[j] == i:
            cc += [cash[j]]
    if (len(cc) > 0):
        sum += max(cc)
print(sum)




# def ks(n, c):
#     cc = cash[n] 
#     tt = time[n]
#     print(f"n: {n}, c: {c}, cc: {cc}, tt: {tt}")
#     if n == 0 or c == 0:
#         result = 0
#     elif tt > c:
#         result = ks(n-1, c)
#     else:
#         t1 = ks(n-1, c)
#         t2 = v + ks(n-1, c-time[n])
#         result = max(t1, t2)
#     print(f"returing {result}")
#     return result
# print(ks(len(data)-1, cap))
