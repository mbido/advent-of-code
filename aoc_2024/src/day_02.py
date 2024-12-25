import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 2

def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)) or all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

def is_safe(levels):
    if not is_sorted(levels):
        return False
    
    prev = levels[0]
    for i in range(1, len(levels)):
        if abs(prev - levels[i]) < 1 or abs(prev - levels[i]) > 3:
            return False
        prev = levels[i]
    return True

def part_1(data):
    res = 0
    for line in data.split("\n"):
        levels = [int(a) for a in line.split(" ")]
        if is_safe(levels):
                res += 1
    return res

def part_2(data):
    res = 0
    for line in data.split("\n"):
        levels = [int(a) for a in line.split(" ")]
        if is_safe(levels):
                res += 1
        else:
            for i in range(len(levels)):
                l = levels[:i] + levels[i + 1:]
                if is_safe(l):
                    res += 1
                    break
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
