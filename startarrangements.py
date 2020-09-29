#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

num = int(next(sys.stdin))

print(f"{num}:")
for i in range(2, num + 1):
    for j in range(i-1, i+1):
        s = i + j
        if (num % s == 0 or num % s == i) and i + j <= num and i - j <= 1:
            print(f"{i},{j}")

