import sys
res = 0
for line in sys.stdin:
    (h, m) = [int(i.strip()) for i in line.split(" ")]
    m_new = (m - 45) % 60
    h_new = (h + ((m - 45) // 60)) % 24
    print(h_new, m_new)

