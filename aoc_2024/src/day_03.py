import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *
import re

YEAR = 2024
DAY = 3

def part_1(data):
    mults = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', data)
    res = 0
    for m in mults:
        m = m[4:]
        m = m[:-1]
        a, b = m.split(",")
        res+= int(a) * int(b)
    return res

def part_2(data):
    mults = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)', data)
    do = True
    res = 0
    for m in mults:
        if m == "do()":
            do = True
            continue
        if m == "don't()":
            do = False
            continue
        if do:
            m = m[4:]
            m = m[:-1]
            a, b = m.split(",")
            res+= int(a) * int(b)
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
