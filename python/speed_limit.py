#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

total = 0
time = 0
for line in sys.stdin:
    line = line.strip()
    sp = line.split(" ")
    if (len(sp) == 1):
        if total != 0:
            print(total, "miles")
        total = 0
        time = 0
    if (len(sp) == 2):
        total += int(sp[0]) * (int(sp[1]) - time)
        time = int(sp[1])
