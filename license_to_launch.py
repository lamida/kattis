#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

inn = sys.stdin
next(inn)
junks = [int(i) for i in next(inn).split(" ")]

mmin = min(junks)

for i in range(len(junks)):
    if junks[i] == mmin:
        print(i)
        break
