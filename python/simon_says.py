#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
inn = sys.stdin
next(inn)

for line in inn:
    if line.startswith("Simon says"):
        print(line.replace("Simon says", "").strip())
