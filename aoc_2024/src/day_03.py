import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 3

def part_1(data):
    return sum(int(a) * int(b) for a, b in re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', data))

def part_2(data):
    mults = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)', data)
    do = True
    res = 0
    for m in mults:
        if m == "do()":
            do = True
        elif m == "don't()":
            do = False
        elif do:
            a, b = re.search(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', m).groups()
            res += int(a) * int(b)
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
