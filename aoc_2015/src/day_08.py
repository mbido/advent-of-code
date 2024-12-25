import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 8

def part_1(data):
    res = 0
    for line in data.split("\n"):
        realSize = len(re.sub(r'(\\\\)|(\\\")|(\\x.{2})', "!", line)) - 2
        res += len(line) - realSize
    return res

def part_2(data):
    res = 0
    for line in data.split("\n"):
        newSize = len(re.sub(r'\"|\\', "!!", line)) + 2
        res += newSize - len(line)
    return res

if __name__ == "__main__":
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
