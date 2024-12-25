import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2023
DAY = 9

def part_1(data):
    #data = as_grid(data)
    for l in data.split("\n"):
        l = nums(l)
    return ""

def part_2(data):
    #data = as_grid(data)
    for l in data.split("\n"):
        l = nums(l)
    return ""

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
