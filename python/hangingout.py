#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

(l, x) = (int(i) for i in next(sys.stdin).split(" "))

cap = 0
exceed = 0
for line in sys.stdin:
    (action, num) = line.split(" ") 
    num = int(num)
    if action == "enter":
        if l < cap + num:
            exceed += 1
        else:
            cap += num
    if action == "leave":
        cap -= num
print(exceed)


