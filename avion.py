#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

idx = 1 
l = []
for line in sys.stdin:
    line = line.lower()
    if "fbi" in line:
        l.append(idx)
    idx+=1
if len(l) == 0:
    print("HE GOT AWAY!")
else:
    print(" ".join([str(i) for i in l]))

