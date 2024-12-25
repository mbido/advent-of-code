import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 12

def set_perimeter(y, x , grid):
    e = get_grid(x, y, grid)
    if e == "?":
        return 0
    res = 0
    for xi, yi in cross_dirs:
        if get_grid(x + xi, y + yi, grid) != e:
            res += 1
    return res


def set_connexe(y, x, grid, connexe, name):
    a = 0
    p = 0
    if grid[y][x] == name and connexe[y][x] == 0 :
        a += 1
        p += set_perimeter(y, x, grid)
        connexe[y][x] = 1
        
    for yi, xi in cross_dirs:
        ok =  1 - get_grid(x + xi, y + yi, connexe, 0)
        if not ok:
            continue
        n = get_grid(x + xi, y + yi, grid)
        if n == name:
            b, c = set_connexe(y + yi, x + xi, grid, connexe, name)
            a += b
            p += c
    return a, p

def part_1(data):
    grid = [list(l) for l in data.split("\n")]
    connexe = [[0 for _ in l] for l in grid]
    res = 0
    for y, l in enumerate(grid):
        for x, n in enumerate(l):
            if connexe[y][x] == 1:
                continue
            a, p = set_connexe(y, x, grid, connexe, n)
            res += a * p
    return res


def get_dirs(n: int):
    res = []
    if n & 1 == 1:
        res.append("N")
    if n & 2 == 2:
        res.append("E")
    if n & 4 == 4:
        res.append("S")
    if n & 8 == 8:
        res.append("O")
    return res

def get_connexe2(y, x, grid, connexe, name):
    a = 0
    p = []
    if grid[y][x] == name and connexe[y][x] == 0 :
        a += 1
        p.append((y, x))
        connexe[y][x] = 1
        
    for yi, xi in cross_dirs:
        ok =  1 - get_grid(x + xi, y + yi, connexe, 0)
        if not ok:
            continue
        n = get_grid(x + xi, y + yi, grid)
        if n == name:
            b, c = get_connexe2(y + yi, x + xi, grid, connexe, name)
            a += b
            p += c
    return a, p

def mask_others(mask, c, coords, map_c, d1, d2):
    y, x = c
    yi, xi = cross_dirs[d1]
    yo1, xo1 = cross_dirs[d2]
    c2 = (y + yi, x + xi)
    c3 = (y + yo1, x + xo1)
    while c2 in coords:
        if c3 in coords:
            return
        map_c[c2] |= mask
        c2 = (c2[0] + yi, c2[1] + xi)
        c3 = (c3[0] + yi, c3[1] + xi)

def compute_perimeter(coords):
    map_c = {c: 0 for c in coords}
    res = 0
    directions = [
        ((-1, 0), 1, [(1, 0), (3, 0)]),
        ((0, 1), 2, [(0, 1), (2, 1)]),
        ((1, 0), 4, [(1, 2), (3, 2)]),
        ((0, -1), 8, [(0, 3), (2, 3)])
    ]
    for c in coords:
        for (dx, dy), bit, masks in directions:
            if map_c[c] & bit == 0 and (c[0] + dx, c[1] + dy) not in coords:
                res += 1
                map_c[c] |= bit
                for args in masks:
                    mask_others(bit, c, coords, map_c, *args)
    return res

def part_2(data):
    grid = [list(l) for l in data.split("\n")]
    connexe = [[0 for _ in l] for l in grid]
    res = 0
    for y, l in enumerate(grid):
        for x, n in enumerate(l):
            if connexe[y][x] == 1:
                continue
            a, p = get_connexe2(y, x, grid, connexe, n)
            p = compute_perimeter(p)
            res += a * p
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
