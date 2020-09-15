#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

inn = sys.stdin

next(inn)

lookup = {"abc": 2, "def": 3, "ghi": 4, "jkl": 5, "mno": 6, "pqrs": 7, "tuv": 8, "wxyz": 9}

def ffind(c):
    for k, v in lookup.items():
        if c in k:
            count = 1
            for x in k:
                if x == c:
                    break
                count += 1
            return str(v) * count
    return "0"

idx = 1
for line in inn:
    line = line.strip()
    prefix = f"Case #{idx}: "
    prefix += ffind(line[0])
    for i in range(len(line) - 1):
        j = i+1
        prev = line[i]
        current = line[j]
        prev_rev = ffind(line[i])
        current_rev = ffind(line[j])
        if current_rev.startswith(prev_rev[0]):
            prefix += " "
        prefix += current_rev
    print(prefix.strip())
    idx += 1


