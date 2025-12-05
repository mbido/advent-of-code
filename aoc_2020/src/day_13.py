import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2020
DAY = 13


def part_1(data):
    #     data = """939
    # 7,13,x,x,59,x,31,19"""
    a, b = data.split("\n")
    a = int(a)
    b = nums(b)
    times = [-a % e for e in b]
    mt = min(times)
    return b[times.index(mt)] * mt


def part_2(data):
    # data = """939
    # 7,13,x,x,59,x,31,19"""
    data = data.split("\n")[1]
    d = 0
    modules = []
    rests = []
    for n in data.split(","):
        if n == "x":
            d += 1
            continue
        modules.append(int(n))
        rests.append(-d)
        d += 1
    return crt(modules, rests)[0]


if __name__ == "__main__":
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
