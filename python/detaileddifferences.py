import sys
inn = sys.stdin
tc = int(next(inn))

for line in inn:
    line = line.strip()
    nl = next(inn).strip()
    output = ""
    for i in range(len(line)):
        if line[i] == nl[i]:
            output+="."
        else:
            output+="*"
    print(line)
    print(nl)
    print(output)
    print()

