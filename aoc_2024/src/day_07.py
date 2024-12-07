import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *
import itertools as it
YEAR = 2024
DAY = 7

def compute(ops, vals):
    res = vals[0]
    for i, v in enumerate(vals[1:]):
        if ops[i] == 0:
            res = res + v
        elif ops[i] == 1:
            res = res * v
        else:
            res = int(str(res) + str(v))
    return res

def is_valid(r, vals, n_ops=2):
    are_sums = list(it.product(list(range(n_ops)), repeat=len(vals)-1))
    for a in are_sums:
        if compute(a, vals) == r:
            return True
    return False

def part_1(data):
    res = 0
    for l in data.split("\n"):
        a, b = l.split(": ")
        a = int(a)
        b = b.split(" ")
        b = [int(e) for e in b]
        if is_valid(a, b):
            res += a
    return res

def part_2(data):
    res = 0
    for l in data.split("\n"):
        a, b = l.split(": ")
        a = int(a)
        b = b.split(" ")
        b = [int(e) for e in b]
        if is_valid(a, b, 3):
            res += a
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
