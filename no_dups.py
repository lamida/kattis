#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
text = next(sys.stdin).strip()

cache = set()
dups = False
for word in text.split(" "):
    if word in cache:
        dups=True
    else:
        cache.add(word)
if dups:
    print("no")
else: 
    print("yes")

