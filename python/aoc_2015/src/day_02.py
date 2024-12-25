import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 2


def part_1(data):
    res = 0
    for line in data.split("\n"):
        l, w, h = list(map(int, line.split("x")))
        res += 2 * l * w + 2 * l * h + 2 * w * h + (l * w * h) // max(l, w, h)
    return res

def part_2(data):
    res = 0
    for line in data.split("\n"):
        l, w, h = list(map(int, line.split("x")))
        res += 2 * (l + w + h) - 2 * max(l, w, h) + l * w * h
    return res


if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
