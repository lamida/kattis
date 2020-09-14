#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

inn = sys.stdin
next(inn)

for line in inn:
    line=line.strip()
    if line == "P=NP":
        print("skipped")
    else:
        print(sum([int(i.strip()) for i in line.split("+")]))
