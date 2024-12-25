import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2016
DAY = 2

def part_1(data):
#     data="""ULL
# RRDDD
# LURDL
# UUUUD"""
    grid = [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
        ]
    pos = (1, 1)
    dirs = {"U":(-1, 0), "R":(0, 1), "D":(1, 0), "L":(0, -1)}
    res = ""
    for l in data.split():
        for c in l:
            d = dirs[c]
            p2 = pos[0] + d[0], pos[1] + d[1]
            a = get_grid(p2[1], p2[0], grid)
            if a != "?":
                pos = p2
        a = get_grid(pos[1], pos[0], grid)
        res += str(a)
    return res

def part_2(data):
    grid = [
        [0, 0, 1, 0, 0],
        [0, 2, 3, 4, 0],
        [5, 6, 7, 8, 9],
        [0, "A", "B", "C", 0],
        [0, 0, "D", 0, 0]
    ]
    pos = (1, 1)
    dirs = {"U":(-1, 0), "R":(0, 1), "D":(1, 0), "L":(0, -1)}
    res = ""
    for l in data.split():
        for c in l:
            d = dirs[c]
            p2 = pos[0] + d[0], pos[1] + d[1]
            a = get_grid(p2[1], p2[0], grid, 0)
            if a != 0:
                pos = p2
        a = get_grid(pos[1], pos[0], grid)
        res += str(a)
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
