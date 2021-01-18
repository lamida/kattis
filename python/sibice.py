#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from math import sqrt

[n, w, h] = [int(i) for i in next(sys.stdin).split(" ")]
d = sqrt(w**2 + h**2)
for line in sys.stdin:
    match = int(line)
    if match < w or match < h or match < d:
        print("DA")
    else:
        print("NE")

