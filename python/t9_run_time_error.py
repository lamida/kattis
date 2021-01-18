#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

inn = sys.stdin

next(inn)

lookup = {}
num = 2
for i in range(ord('a'), ord('p'), 3):
    lookup[str(num)] = [chr(i), chr(i+1), chr(i+2)]
    num+=1
lookup["7"] = ['p', 'q', 'r', 's']
lookup["8"] = ['t', 'u', 'v']
lookup["9"] = ['w', 'x', 'y', 'z']

reverse_lookup = {}
for k,v in lookup.items():
    key = k
    for vv in v:
        reverse_lookup[vv] = key
        key += k

reverse_lookup[' '] = '0'

idx = 1
for line in inn:
    line = line.rstrip("\n")
    prefix = f"Case #{idx}: "
    prefix += reverse_lookup[line[0]]
    for i in range(len(line) - 1):
        j = i+1
        prev = line[i]
        current = line[j]
        prev_rev = reverse_lookup[line[i]]
        current_rev = reverse_lookup[line[j]]
        if current_rev.startswith(prev_rev[0]):
            prefix += " "
        prefix += current_rev
    print(prefix.strip())
    idx += 1

