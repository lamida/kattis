#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

inn = sys.stdin
next(inn)
for line in inn:
    [a, b, c] = [int(i) for i in line.split(" ")]
    if a + b == c or a-b == c or b-a==c or a * b == c or a/b == c or b/a==c:
        print("Posible")
    else:
        print("Imposible")
