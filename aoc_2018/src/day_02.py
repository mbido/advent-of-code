import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2018
DAY = 2

def part_1(data):
    az = "abcdefghijklmnopqrstuvwxyz"
    res = [0, 0]
    for l in data.split():
        two = False
        three = False
        for c in az:
            count = l.count(c)
            if count == 2:
                two = True
            elif count == 3:
                three = True
        if two:
            res[0] += 1
        if three:
            res[1] += 1
    return res[0] * res[1]

def are_close(a, b):
    ok = True
    for i, c in enumerate(a):
        if b[i]!=c:
            if not ok:
                return False
            ok = False
    return True

def compute(a, b):
    res = ""
    for i, c in enumerate(a):
        if b[i]==c:
            res += c
    return res

def part_2(data):
    d = data.split()
    for i, l1 in enumerate(d):
        for l2 in d[i+1:]:
            if are_close(l1, l2):
                return compute(l1, l2)
    return "ERROR"

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
