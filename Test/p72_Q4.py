#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'circles' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY info as parameter.
#

def circles(info):
    # Write your code here
    res = []
    for line in info:
        x1, y1, r1, x2, y2, r2 = tuple([int(x) for x in line.split(" ")])
        ub = r1 + r2
        lb = abs(r1 - r2)
        d = max(abs(x1 - x2), abs(y1 - y2))
        if (d == 0):
            res.append("Concentric")
        elif (d > ub):
            res.append("Disjoint-Outside")
        elif (d == ub or d == lb):
            res.append("Touching")
        elif (d > lb):
            res.append("Intersecting")
        else:
            assert d < lb
            res.append("Disjoint-Inside")
        continue
    return (res)


