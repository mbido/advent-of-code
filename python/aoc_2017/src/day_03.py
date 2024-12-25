import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2017
DAY = 3

def part_1(data):
    x = int(data)
    k = int((math.sqrt(x) - 1) / 2) + 1
    n = (2 * k + 1) ** 2
    c = [n - i * 2 * k for i in range(4)]
    d = min([abs(a - x) for a in c])
    return 2 * k - d

def part_2(data):
    for l in data.split("\n"):
        l = nums(l)
    return ""

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
