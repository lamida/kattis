import sys
inn = sys.stdin
next(inn)

for line in inn:
    (b, p) = (float(i) for i in line.strip().split(" "))
    abpm = 60.0 / p
    bpm = 60 * b / p
    print("%.4f %.4f %.4f" % (bpm - abpm, bpm, bpm + abpm))
