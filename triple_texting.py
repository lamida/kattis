#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

inn = next(sys.stdin).strip()
size = int(len(inn)/3)
i, j, k = 0, size, 2 * size
res = ""
while i < size:
    cache = {}
    for x in (inn[i], inn[j], inn[k]):
        if cache.get(x) is None:
            cache[x] = 1
        else:
            cache[x] += 1
    if len(cache) == 1:
        res += inn[i]
    else:
        for z,v in cache.items():
            if v == 2:
                res += z
    i+=1
    j+=1
    k+=1
print(res.strip())
