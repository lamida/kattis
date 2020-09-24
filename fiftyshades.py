#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

inn = sys.stdin

next(inn)

count = 0
for line in inn:
    line = line.lower()
    if "pink" in line or "rose" in line:
        count += 1
if count > 0:
    print(count)
else:
    print("I must watch Star Wars with my daughter")
