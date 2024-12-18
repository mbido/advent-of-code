import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2018
DAY = 1

def part_1(data):
    return sum([int(elt) for elt in data.split("\n")])

def part_2(data):
    current = 0
    f = [int(elt) for elt in data.split("\n")]

    fs = set()

    while(True):
        for elt in f:
            if current in fs:
                return current
            fs.add(current)
            current += elt
    return "ERROR"

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
