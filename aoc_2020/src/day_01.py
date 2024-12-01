import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2020
DAY = 1

def part_1(data):
    d = [int(elt) for elt in data.split("\n")]
    for i in range(len(d)):
        for j in range(i, len(d)):
            if d[i] + d[j] == 2020:
                return d[i] * d[j]
    return "ERROR"

def part_2(data):
    d = [int(elt) for elt in data.split("\n")]
    for i in range(len(d)):
        for j in range(i, len(d)):
            for k in range(j, len(d)):
                if d[i] + d[j] + d[k] == 2020:
                    return d[i] * d[j] * d[k]
    return "ERROR"

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
