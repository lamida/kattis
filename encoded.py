#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from math import sqrt
next(sys.stdin)

def rotate_left(mat, size):
    matrix = [["_" for i in range(size)] for j in range(size)]
    right = size - 1
    for i in range(size):
        for j in range(size):
            matrix[i][j] = mat[j][right]
        right -= 1
    result = ""
    for i in range(size):
        for j in range(size):
            result += matrix[i][j]
    return result


for line in sys.stdin:
    line = line.strip()
    size = int(sqrt(len(line)))
    matrix = [["_" for i in range(size)] for j in range(size)]
    x = 0
    for i in range(size):
        for j in range(size):
            matrix[i][j] = line[x]
            x += 1
    print("".join(rotate_left(matrix, size)))

