import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2020
DAY = 2

def part_1(data):
    res = 0
    for line in data.split("\n"):
        mn, mx, c, pwd = re.match(r'([0-9]+)\-([0-9]+) ([a-z])\: ([a-z]+)', line).groups()
        if int(mn) <= pwd.count(c) <= int(mx):
            res += 1
    return res

def part_2(data):
    res = 0
    for line in data.split("\n"):
        mn, mx, c, pwd = re.match(r'([0-9]+)\-([0-9]+) ([a-z])\: ([a-z]+)', line).groups()
        a = pwd[int(mn)-1]
        b = pwd[int(mx)-1]
        if a != b and (a == c or b == c):
            res += 1
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
