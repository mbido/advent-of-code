import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 25

data = aoct.get_input(YEAR, DAY)

res = 0
Keys = []
Locks = []
for g in data.split("\n\n"):
    g = [[c for c in r] for r in g.split("\n")]
    if g[0].count("#") == 5:
        Locks.append(g)
    else:
        Keys.append(g)

def to_cols(grid):
    res = []
    for x in range(len(grid[0])):
        height = 0
        for y in range(len(grid)):
            if grid[y][x] == "#":
                height += 1
        res.append(height - 1)
    return res

c_Keys = list(map(to_cols, Keys))
c_Locks = list(map(to_cols, Locks))

def does_match(key, lock):
    for i in range(len(key)):
        if key[i] + lock[i] > 5:
            return False 
    return True

for k in c_Keys:
    for l in c_Locks:
        # print(f"k={k}, l={l} -> {does_match(k, l)}")
        if does_match(k, l):
            res += 1

print(res)
