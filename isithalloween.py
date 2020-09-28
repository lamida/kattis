import sys

text = next(sys.stdin).strip()
if text == "OCT 31" or text == "DEC 25":
    print("yup")
else:
    print("nope")

