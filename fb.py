import sys

inn = sys.stdin

for line in inn:
    line = line.strip()
    (x, y, n) = (int(i) for i in line.split(" "))
    for i in range(1, n+1):
        if i % x == 0 and i % y == 0:
            print("FizzBuzz")
        elif i % x == 0:
            print("Fizz")
        elif i % y == 0:
            print("Buzz")
        else:
            print(i)

