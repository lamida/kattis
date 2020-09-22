#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
word = next(sys.stdin).strip()

hiss = False
for i in range(len(word)-1):
    j = i+1
    if word[i] == "s" and word[j] == "s":
        hiss = True
        break
    
if hiss:
    print("hiss")
else:
    print("no hiss")

