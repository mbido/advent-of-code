import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2021
DAY = 2

def part_1(data):
    pos = depth = 0
    for line in data.split("\n"):
        i, v = line.split(" ")
        if i[0] == "f":
            pos += int(v)
        elif i[0] == "u":
            depth -= int(v)
        else:
            depth += int(v)
    return pos * depth

def part_2(data):
    aim = pos = depth = 0
    for line in data.split("\n"):
        i, v = line.split(" ")
        if i[0] == "f":
            pos += int(v)
            depth += aim * int(v)
        elif i[0] == "u":
            aim -= int(v)
        else:
            aim += int(v)
    return pos * depth

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
