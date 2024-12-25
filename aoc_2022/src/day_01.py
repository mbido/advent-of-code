import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2022
DAY = 1

def part_1(data):
    elves = data.split("\n\n")
    res = []
    for i in range(len(elves)):
        res.append(sum(int_lines(elves[i])))
    res.sort(reverse=True)
    return res[0]

def part_2(data):
    elves = data.split("\n\n")
    res = []
    for i in range(len(elves)):
        res.append(sum(int_lines(elves[i])))
    res.sort(reverse=True)
    return sum(res[:3])

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
