import sys

next(sys.stdin)

for line in sys.stdin:
    alpha = dict((chr(i), False) for i in range(ord('a'), ord('z') + 1))
    line = line.strip().lower()
    for i in line:
        alpha[i] = True
    missing = ""
    for k,v in alpha.items():
        if not v:
            missing += k
    if len(missing) == 0:
        print("pangram")
    else:
        print("missing", missing)
