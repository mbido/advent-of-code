import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2017
DAY = 1

def part_1(data):
    # data = "1111"
    res = 0
    for i in range(len(data)):
        if data[i] == data[(i + 1) % len(data)]:
            res += int(data[i])
    return res

def part_2(data):
    res = 0
    for i in range(len(data)):
        if data[i] == data[(i + len(data) // 2) % len(data)]:
            res += int(data[i])
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
