import sys

inn = sys.stdin
next(inn)

bats = [int(i) for i in next(inn).strip().split(" ")]
clean_bats = list(filter(lambda x: x != -1, bats))
print(sum(clean_bats)/len(clean_bats))

