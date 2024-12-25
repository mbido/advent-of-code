import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 10

def one_pass(nbString):
    res = ""
    counter = 0
    last = ""
    for i in range(len(nbString)):
        if nbString[i] == last:
            counter += 1
        else:
            res += str(counter) + last
            counter = 1
            last = nbString[i]
    res += str(counter) + last
    return res[1::]

def part_1(data):
    for _ in range(40):
        data = one_pass(data)
    return len(data)

def part_2(data):
    for _ in range(50):
        data = one_pass(data)
    return len(data)

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
