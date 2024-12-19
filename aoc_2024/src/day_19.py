import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 19

def part_1(data):
    s1, s2 = data.split("\n\n")
    r = "^(" + "|".join(s1.split(", ")) + ")+$"
    return len([line for line in s2.split("\n") if re.match(r, line)])

mem = {}

def possible(patterns, line):
    if line in mem:
        return mem[line]
    res = 0
    for p in patterns:
        if p == line:
            res += 1
        elif line.startswith(p):
            res += possible(patterns, line[len(p):])
    mem[line] = res
    return res

def part_2(data):
    s1, s2 = data.split("\n\n")
    s1 = s1.split(", ")
    s2 = s2.split("\n")
    res = 0
    for l in s2:
        res += possible(s1, l)
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
