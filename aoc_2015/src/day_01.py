import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 1


def part_1(data):
    up = data.count("(")
    down = data.count(")")
    return up - down


def part_2(data):
    level = 0
    for index, char in enumerate(data):
        if char == "(":
            level += 1
        else:
            level -= 1
        if level == -1:
            return index + 1
    return -1


if __name__ == "__main__":
    start = time.perf_counter()
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
    print(f"Executed in {time.perf_counter() - start}s")
