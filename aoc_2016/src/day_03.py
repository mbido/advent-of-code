import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2016
DAY = 3

def valid(a, b, c):
    return a+b > c and a+c > b and b+c > a

def part_1(data):
    res = 0
    for l in data.split("\n"):
        a, b, c = nums(l)
        res = res + 1 if valid(a, b, c) else res
    return res

def part_2(data):
    res = 0
    d = data.split("\n")
    for i in range(0, len(d), 3):
        c = nums(" ".join(d[i:i+3]))
        res += sum([int(valid(c[i], c[i + 3], c[i + 6])) for i in range(3)])
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
