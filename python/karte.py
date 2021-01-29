import sys
inn = next(sys.stdin).strip()

d = {
    "P": 0,
    "K": 0,
    "H": 0,
    "T": 0,
}
seen = []
greska=False
for i in range(0, len(inn), 3):
    current = inn[i:i+3]
    if current in seen:
        print("GRESKA")
        greska=True
        break
    d[current[0]] += 1
    seen += [current]
if not greska:
    print(13-d["P"], 13-d["K"], 13-d["H"], 13-d["T"])
    