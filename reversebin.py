#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

inn = int(next(sys.stdin))

bb = [str(i) for i in bin(inn)[2:]]

i = 0
j = len(bb) - 1
while i < j:
    bb[i], bb[j] = bb[j], bb[i]
    i+=1
    j-=1

print(int("".join(bb), 2))

