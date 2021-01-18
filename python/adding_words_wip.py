import sys

inn = sys.stdin

vars = {}
for line in inn:
    line = line.strip()
    tokens = line.split(" ")
    if tokens[0] == "def":
        vars[tokens[1]] = tokens[2]
    elif tokens[0] == "calc":
        sum = int(tokens[1])
        for i in range(2,len(tokens[1:]) - 1):
            j = i + 1




    else:
        vars = {}


