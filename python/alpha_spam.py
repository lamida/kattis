#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

text = next(sys.stdin).strip()

dd = {
    "ws": 0,
    "low": 0,
    "up": 0,
    "sym": 0
}
for i in text:
    if i == "_":
        dd["ws"] += 1
    elif i.islower():
        dd["low"] += 1
    elif i.isupper():
        dd["up"] += 1
    else:
        dd["sym"] += 1

l = len(text)
print(dd["ws"]/l)
print(dd["low"]/l)
print(dd["up"]/l)
print(dd["sym"]/l)
