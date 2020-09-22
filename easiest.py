#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

for line in sys.stdin:
    N = int(line)
    if N == 0:
        break
    ssum = sum([int(i) for i in str(N)])
    p = 11
    while True:
        result = p * N
        bsum = sum([int(i) for i in str(result)]) 
        if bsum == ssum:
            print(p)
            break
        p+=1



