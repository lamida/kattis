#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

inn = next(sys.stdin).strip()
a, b, c = [int(i) for i in inn.split(" ")]

ssum = 0

if b - a > c - b:
    while b - a > 1:
        c = b
        b -= 1
        ssum += 1
else:
    while c - b > 1:
        a = b
        b += 1
        ssum += 1
print(ssum)

