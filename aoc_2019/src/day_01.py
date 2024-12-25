import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2019
DAY = 1

def part_1(data):
    d = [int(elt) for elt in data.split("\n")]
    res = 0
    for elt in d:
        res += elt//3 - 2
    return res

def part_2(data):
    d = [int(elt) for elt in data.split("\n")]
    res = 0
    for elt in d:
        f = elt//3 - 2
        while f > 0:
            res += f 
            f = f // 3 -2
    
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
