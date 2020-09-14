#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sset = set()
for i in sys.stdin:
    i = int(i)
    sset.add(i % 42)
print(len(sset))
