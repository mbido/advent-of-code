import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 11

def blink(n):
    if n == 0:
        return [1]
    str_n = str(n)
    l = len(str_n)
    if l % 2 == 0:
        return [int(str_n[:l//2]), int(str_n[l//2:])]
    return [n * 2024]

map = {}

def recursive(n, repeat):
    global map
    if repeat == 1:
        return len(blink(n))
    key = (n, repeat)
    if key in map:
        return map[key]
    t = blink(n)
    res = sum(recursive(l, repeat - 1) for l in t)
    map[key] = res
    return res

def part_1(data):
    global map
    tab = [int(n) for n in data.split(" ")]
    res = 0
    for n in tab:
        map = {}
        res += recursive(n, 25)
    return res

def part_2(data):
    global map
    tab = [int(n) for n in data.split(" ")]
    res = 0
    for n in tab:
        map = {}
        res += recursive(n, 75)
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
