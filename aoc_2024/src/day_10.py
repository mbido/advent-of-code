import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 10

def go_to_9(grid, y, x):
    res = set()
    e = grid[y][x]
    if e == 9:
        res.add((y, x))
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for yi, xi in dirs:
        v = get_grid(x + xi, y + yi, grid, -1)
        if v == e + 1:
            eds = list(go_to_9(grid, y + yi, x + xi))
            for elt in eds:
                # print(elt)
                res.add(elt)
    return res

def part_1(data):
    grid = [[int(e) for e in list(l)] for l in data.split()]
    heads = []
    for y, l in enumerate(grid):
        for x, c in enumerate(l):
            if c == 0:
                heads.append((y, x))
                
    res = 0
    for y, x in heads:
        ends = list(go_to_9(grid, y, x))
        res += len(ends)
    return res

def go_to_9_v2(grid, y, x):
    res = []
    e = grid[y][x]
    if e == 9:
        res.append((y, x))
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for yi, xi in dirs:
        v = get_grid(x + xi, y + yi, grid, -1)
        if v == e + 1:
            eds = go_to_9_v2(grid, y + yi, x + xi)
            for elt in eds:
                res.append(elt)
    return res

def part_2(data):
    grid = [[int(e) for e in list(l)] for l in data.split()]
    heads = []
    for y, l in enumerate(grid):
        for x, c in enumerate(l):
            if c == 0:
                heads.append((y, x))
                
    res = 0
    for y, x in heads:
        ends = go_to_9_v2(grid, y, x)
        res += len(ends)
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
