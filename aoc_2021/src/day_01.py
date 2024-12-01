import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2021
DAY = 1

def part_1(data):
    d = [int(elt) for elt in data.split("\n")]
    return len([d[i] for i in range(1, len(d)) if d[i - 1] < d[i]])

def part_2(data):
    d = [int(elt) for elt in data.split("\n")]
    prev = sum(d[:3])
    res = 0
    for i in range(1, len(d)-2):
        current = sum(d[i:i+3])
        if current > prev:
            res += 1
        prev = current
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
