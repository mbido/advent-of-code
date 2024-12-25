import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 20

data = aoct.get_input(YEAR, DAY)

res = 0

grid = as_grid(data)

S = (-1, -1)
for y, r in enumerate(grid):
    for x, c in enumerate(r):
        if c == "S":
            S = (y, x)
            break
    if S != (-1, -1):
        break

q = [S]
v = {S : 0}  
while q:
    pos = q.pop()
    w = v[pos]
    for y, x in adj4:
        p2 = (pos[0] + y, pos[1] + x)
        if p2 in v or get_grid(p2, grid, "#") == "#":
            continue
        v[p2] = w + 1
        q.insert(0, p2)

res = 0
for pos in v:
    for y, x in adj4:
        p2 = (pos[0] + y * 2, pos[1] + x * 2)
        if p2 in v and v[pos] + 2 <= v[p2] - 100:
            res += 1
print(res)

def bfs(S, grid):
    q = [S]
    v = {S : 0}  
    res = set()
    while q:
        pos = q.pop()
        w = v[pos]
        for y, x in adj4:
            p2 = (pos[0] + y, pos[1] + x)
            if p2 in v:
                continue
            g = get_grid(p2, grid)
            if p2 not in res and (g == "." or g == "E" or g == "S"):
                res.add(p2)
            if w + 1 < 20:
                q.insert(0, p2)
            v[p2] = w + 1
    return res, v


N = 100

res = 0
for p in v:
    w1 = v[p]
    r2, v2 = bfs(p, grid)
    for r in r2:
        w2 = v[r]
        if w2 - w1 - v2[r] >= N:
            res += 1
print(res)