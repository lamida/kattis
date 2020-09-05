import sys
stone = int(next(sys.stdin).strip())

print("Alice" if stone % 2 != 0 else "Bob")
