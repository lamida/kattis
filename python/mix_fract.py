#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

for line in sys.stdin:
    [num, denom] = [int(i) for i in line.split(" ")]
    if num == 0 and denom == 0:
        break
    print(num//denom, num%denom, "/", denom)
