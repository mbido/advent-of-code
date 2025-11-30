import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 18

data = aoct.get_input(YEAR, DAY)

start = time.perf_counter()

# print(data)
res = 0

g1 = as_grid(data)
g2 = copy.deepcopy(g1)


def lives(pos, grid):
    l = 0
    on = grid[pos[0]][pos[1]] == "#"
    for y, x in adj8:
        p = (pos[0] + y, pos[1] + x)
        if get_grid(p, grid) == "#":
            l += 1
    if on and 2 <= l <= 3:
        return True
    return l == 3


def step(g1, g2):
    for y, r in enumerate(g1):
        for x, c in enumerate(r):
            g2[y][x] = "#" if lives((y, x), g1) else "."


for _ in range(50):
    step(g1, g2)
    step(g2, g1)

print("".join(["".join(r) for r in g1]).count("#"))

g1 = as_grid(data)
g2 = copy.deepcopy(g1)

corners = [(0, 0), (0, len(g1) - 1), (len(g1) - 1, 0), (len(g1) - 1, len(g1) - 1)]

for y, x in corners:
    g1[y][x] = "#"
    g2[y][x] = "#"


def step(g1, g2):
    for y, r in enumerate(g1):
        for x, c in enumerate(r):
            p = (y, x)
            g2[y][x] = "#" if lives(p, g1) or p in corners else "."


for i in range(50):
    step(g1, g2)
    step(g2, g1)


print("".join(["".join(r) for r in g1]).count("#"))
print(f"Executed in : {time.perf_counter() - start}s")
