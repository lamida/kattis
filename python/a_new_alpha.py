import sys

inn = next(sys.stdin).strip().lower()
ddict = {
    "a": "@",
    "b": "8",
    "c": "(",
    "d": "|)",
    "e": "3",
    "f": "#",
    "g": "6",
    "h": "[-]",
    "i": "|",
    "j": "_|",
    "k": "|<",
    "l": "1",
    "m": "[]\/[]",
    "n":"[]\[]",
    "o":"0",
    "p":"|D",
    "q":"(,)",
    "r":"|Z",
    "s":"$",
    "t":"']['",
    "u":"|_|",
    "v": "\/",
    "w": "\/\/",
    "x": "}{",
    "y": "`/",
    "z": "2"
}

res = ""
for i in inn:
    if ddict.get(i) is None:
        res += i
    else:
        res += ddict[i]
print(res)