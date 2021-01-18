#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

inn = next(sys.stdin).strip()

cache = {}
ranks = "A23456789TJQK"
for c in ranks:
    cache[c] = 0

for card in inn.split(" "):
    cache[card[0]] += 1

mmax = 0
for k, v in cache.items():
    if v > mmax:
        mmax = v


print(mmax)
