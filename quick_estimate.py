#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

inn = sys.stdin
next(inn)
for line in inn:
    print(len(line.strip()))
