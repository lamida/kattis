#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

inn = sys.stdin
next(inn)
cache = {}
for line in inn:
    line = line.strip()
    a, b = line.split(" ")
    if b.isnumeric():
        cache[int(b)] = a
    else:
        cache[int(a)//2] = b
idx = sorted(list(cache.keys()))
for i in idx:
    print(cache[i])
