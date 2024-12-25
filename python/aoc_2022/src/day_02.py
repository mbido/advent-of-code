import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2022
DAY = 2

def part_1(data):
    res = 0
    for line in data.split("\n"):
        a, b = line.split(" ")
        a = ord(a) - ord("A") + 1
        b = ord(b) - ord("X") + 1
        if a == b:
            res += b + 3
        elif b == a % 3 + 1:
            res += b + 6
        else:
            res += b
    return res

def part_2(data):
    res = 0
    for line in data.split("\n"):
        a, b = line.split(" ")
        a = ord(a) - ord("A") + 1
        win = a % 3 + 1
        lose = (a + 1) % 3 + 1
        if b == "Y":
            res += a + 3
        elif b == "X":
            res += lose
        else:
            res += win + 6
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
