import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 4

def get(x, y, grid):
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        return grid[y][x]
    return "?"

def check(x, x_sign, y, y_sign, grid):
    m = "XMAS"
    for i in range(len(m)):
        if get(x + x_sign * i, y + y_sign * i, grid) != m [i]:
            return False
    return True

def count_XMAS(x, y, grid):
    res = []
    signs = [-1, +1, 0]
    for x_sign in signs:
        for y_sign in signs:
            res.append(check(x, x_sign, y, y_sign, grid))
    return sum(res)

def part_1(data):
    res = 0
    grid = data.split("\n")
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "X":
                res += count_XMAS(x, y, grid)
    return res

def is_X_MAS(x, y, grid):
    ms = ["MAS", "SAM"]
    a = get(x- 1, y - 1, grid) + get(x, y, grid) + get(x + 1, y + 1, grid)
    b = get(x + 1, y - 1, grid) + get(x, y, grid) + get(x - 1, y + 1, grid)
    return a in ms and b in ms

def part_2(data):
    res = []
    grid = data.split("\n")
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "A":
                res.append(is_X_MAS(x, y, grid))
    return sum(res)

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
