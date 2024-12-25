import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 7

def helper(data, wire, save = {}):
    if re.match(r'[0-9]+', wire):
        return int(wire), save
    if wire in save:
        return save[wire], save
    l = ""
    for line in data.split("\n"):
        if line.split("-> ")[1] == wire:
            l = line
            break
    expr = l.split(" -> ")[0]
    if "AND" in expr:
        a, b = expr.split(" AND ")
        ha, save = helper(data, a, save)
        hb, save = helper(data, b, save)
        res = int(ha) & int(hb)
        save[wire] = res
        return res, save
    if "OR" in expr:
        a, b = expr.split(" OR ")
        ha, save = helper(data, a, save)
        hb, save = helper(data, b, save)
        res = int(ha) | int(hb)
        save[wire] = res
        return res, save
    if "LSHIFT" in expr:
        a, b = expr.split(" LSHIFT ")
        ha, save = helper(data, a, save)
        hb, save = helper(data, b, save)
        res = int(ha) << int(hb)
        save[wire] = res
        return res, save
    if "RSHIFT" in expr:
        a, b = expr.split(" RSHIFT ")
        ha, save = helper(data, a, save)
        hb, save = helper(data, b, save)
        res = int(ha) >> int(hb)
        save[wire] = res
        return res, save
    if "NOT" in expr:
        a = expr.split("NOT ")[1]
        ha, save = helper(data, a, save)
        res = ~int(ha) & 0xffff
        save[wire] = res
        return res, save
    ha, save = helper(data, expr, save)
    save[wire] = int(ha)
    return int(ha), save

def part_1(data):
    return helper(data, "a")[0]

def part_2(data):
    return helper(data, "a", {"b" : helper(data, "a")[0]})[0]

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)