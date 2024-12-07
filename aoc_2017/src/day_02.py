import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2017
DAY = 2

def part_1(data):
    res = 0
    for l in data.split("\n"):
        vals = [int(e) for e in l.split()]
        res += max(vals) - min(vals)
    return res

def part_2(data):
    res = 0
    for l in data.split("\n"):
        vals = sorted([int(e) for e in l.split()], reverse=True)
        for i, v1 in enumerate(vals[:-1]):
            for v2 in vals[i+1:]:
                if v1 / v2 == v1//v2:
                    res += v1//v2
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
