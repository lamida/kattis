import sys

inn = sys.stdin

next(inn)

trees = [int(i) for i in next(inn).split(" ")]

rev_trees = sorted(trees, reverse=True)
for i in range(1, len(trees) + 1):
    rev_trees[i - 1] += i
print(max(rev_trees) + 1)