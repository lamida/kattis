import sys

text = next(sys.stdin).strip()

result = ""
i = 0
while i  < len(text):
    j = i + 1
    k = i + 2
    if j < len(text) and k < len(text) and text[j] == "p" and text[i] in "aiueo" and text[k] in "aiueo" and text[i] == text[k]:
        result += text[i]
        i += 3
    else:
        result += text[i]
        i += 1
print(result)