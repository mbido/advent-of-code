import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 4


def allZeros(s):
    for char in s:
        if char != "0":
            return False
    return True

def part_1(data):
    suffix = 0
    while not allZeros(md5(data + str(suffix))[:5:]):
        suffix += 1
    return suffix

def part_2(data):
    suffix = 0
    while not allZeros(md5(data + str(suffix))[:6:]):
        suffix += 1
    return suffix



if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
