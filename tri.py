import sys

a, b, c = (int(i) for i in next(sys.stdin).split(" "))
if a + b == c:
    print(str(a)+"+"+str(b)+"="+str(c))
elif a - b == c:
    print(str(a)+"-"+str(b)+"="+str(c))
elif a * b == c:
    print(str(a)+"*"+str(b)+"="+str(c))
elif a // b == c:
    print(str(a)+"/"+str(b)+"="+str(c))
elif a==b+c:
    print(str(a)+"="+str(b)+"+"+str(c))
elif a==b-c:
    print(str(a)+"="+str(b)+"-"+str(c))
elif a==b*c:
    print(str(a)+"="+str(b)+"*"+str(c))
elif a==b//c:
    print(str(a)+"="+str(b)+"/"+str(c))
