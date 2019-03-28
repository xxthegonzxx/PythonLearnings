#!/usr/bin/env python3
import math
import operator
import functools
from bisect import bisect


def iqm(file_path):
    arr = []
    with open(file_path, "r") as file:
        for line in file:
            intLine = int(line)
            index = bisect(arr, intLine)
            arr.insert(index, intLine)
            if len(arr) >= 4:
                quartile = len(arr) / 4.0
                ys = arr[int(math.ceil(quartile))-1:int(math.floor((3*quartile)))+1]
                factor = quartile - (len(ys)/2.0 - 1)
                mean = (functools.reduce(operator.add, ys[1:-1], 0) + (ys[0] + ys[-1]) * factor) / (2*quartile)
                print("%d: %.2f" % (len(arr), mean))
    file.close()
