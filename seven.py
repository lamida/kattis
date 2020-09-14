#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

inn = next(sys.stdin).strip()

cache = {
    "T": 0,
    "C": 0,
    "G": 0,
}


for i in inn:
    cache[i] += 1


sum = 0
mmin = cache['T']
for k, v in cache.items():
    sum += v ** 2
    if v < mmin:
        mmin = v

total = sum + 7 * mmin
print(total)
