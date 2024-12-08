import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 8

def print_grid(grid):
    for r in grid:
        p = ""
        for c in r:
            p += c
        print(p)
    print()
    
def compute_locations(grid1):
    locations = {}
    for i, r in enumerate(grid1):
        for j, c in enumerate(r):
            if c == ".":
                continue
            if c in locations:
                locations[c].add((i, j))
            else:
                locations[c] = set()
                locations[c].add((i,j))
    return locations

def part_1(data):
    grid1 = [list(l) for l in data.split("\n")]
    grid2 = [[0 for _ in range(len(grid1[0]))] for _ in grid1]
    locations = compute_locations(grid1);
    
    for c in locations:
        for a in locations[c]:
            for b in locations[c]:
                if a == b:
                    continue
                diff_x = a[1] - b[1]
                diff_y = a[0] - b[0]
                set_grid(a[1] + diff_x, a[0] + diff_y, grid2, 1)

    return sum([sum(l) for l in grid2])

def part_2(data):
    grid1 = [list(l) for l in data.split("\n")]
    grid2 = [[0 for _ in range(len(grid1[0]))] for _ in grid1]
    locations = compute_locations(grid1)
    
    for c in locations:
        for a in locations[c]:
            for b in locations[c]:
                if a == b:
                    set_grid(a[1], a[0], grid2, 1)
                    continue
                diff_x = a[1] - b[1]
                diff_y = a[0] - b[0]
                x = a[1] + diff_x
                y = a[0] + diff_y
                while 0 <= x < len(grid2[0]) and 0 <= y < len(grid2):
                    set_grid(x, y, grid2, 1)
                    x += diff_x
                    y += diff_y
                    
    return sum([sum(l) for l in grid2])

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
