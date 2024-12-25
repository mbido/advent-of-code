import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2023
DAY = 2

def parse(cols, g):
    c = [0, 0, 0]
    for n, j in re.findall(r'([0-9]+) ([a-z]+)', g):
        c[cols.index(j)] += int(n)
    return c

def part_1(data):
    cols = ["blue", "red", "green"]
    lim = [14, 12, 13]
    res  = 0
    for i, l in enumerate(data.split("\n")):
        l = l.split(";")
        valid = True
        for g in l:
            c = parse(cols, g)
            if sum([int(a <= b) for a, b in zip(c, lim)]) != 3:
                valid = False
        if valid :
            res += i + 1
    return res

def part_2(data):
    cols = ["blue", "red", "green"]
    res  = 0
    for l in data.split("\n"):
        l = l.split(";")
        cmin = [0, 0, 0]
        for g in l:
            c = parse(cols, g)
            cmin = [max(c[i], cmin[i]) for i in range(3)]
        res += reduce(lambda a, b : a * b, cmin)
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
