import sys
l = next(sys.stdin).split()

def ssort(l):
    swapped = True
    while swapped:
        swapped = False
        for y in range(1, len(l)):
            x = y - 1
            if l[y] < l[x]:
                swapped |= True
                l[x], l[y] = l[y], l[x]
                print(" ".join(l))


if __name__ == "__main__":
    # ssort([2,1,5,3,4])
    # ssort([2,3,4,5,1])
    ssort(l)