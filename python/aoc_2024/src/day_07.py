import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *
YEAR = 2024
DAY = 7

def is_valid(r, vals, n_ops=2):
    return recurrence(r, vals[1:], n_ops, vals[0])

def recurrence(r, vals, n_ops, res):
    if len(vals) == 0:
        return r == res
    
    r_add = res + vals[0]
    r_mul = res * vals[0]
    r_con =  int(str(res) + str(vals[0]))
    if recurrence(r, vals[1:], n_ops, r_add) or recurrence(r, vals[1:], n_ops, r_mul):
        return True
    if n_ops == 3 and recurrence(r, vals[1:], n_ops, r_con):
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
