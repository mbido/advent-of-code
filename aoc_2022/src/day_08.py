import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2022
DAY = 8

data = aoct.get_input(YEAR, DAY)

res = 0

# graphs
# V = list(set(re.findall(r'[a-z]{2}', data)))
# V_T = {V[i] : i for i in range(len(V))}
# edges = [(V_T[a], V_T[b]) for a, b in re.findall(r'([a-z]{2})\-([a-z]{2})', data)]
# G = ig.Graph(edges=edges, directed=False)
# edges = [(V_T[a], V_T[b], int(c)) for a, b, c in re.findall(r'([a-z]{2})\-([a-z]{2})\-(\d+)', data)]
# G = ig.Graph(edges=[(s,t) for s,t,_ in edges], directed=False, edge_attrs={"weight": [w for _,_,w in edges]})

# data = """30373
# 25512
# 65332
# 33549
# 35390"""

data = as_grid(data, type=int)
res += len(data) * 2 + len(data[0]) * 2 - 4


def is_visible(i, j, grid):
    elt = grid[i][j]

    l = [grid[i][j - k - 1] for k in range(j)]
    r = [grid[i][j + k + 1] for k in range(len(grid[0]) - j - 1)]
    u = [grid[i - k - 1][j] for k in range(i)]
    d = [grid[i + k + 1][j] for k in range(len(grid) - i - 1)]

    for n in [l, r, u, d]:
        if all([elt > t for t in n]):
            return 1
    return 0


for i in range(1, len(data) - 1):
    for j in range(1, len(data[0]) - 1):
        res += is_visible(i, j, data)

print(res)

res = 0


def get_score(i, j, grid):
    score = 1
    elt = grid[i][j]

    l = [grid[i][j - k - 1] for k in range(j)]
    r = [grid[i][j + k + 1] for k in range(len(grid[0]) - j - 1)]
    u = [grid[i - k - 1][j] for k in range(i)]
    d = [grid[i + k + 1][j] for k in range(len(grid) - i - 1)]

    for n in [l, r, u, d]:
        idx = 0
        here = 0
        # print(n)
        while idx < len(n):
            if n[idx] >= elt:
                here += 1
                break
            here += 1
            idx += 1
        score *= here

    return score


for i in range(1, len(data) - 1):
    for j in range(1, len(data[0]) - 1):
        res = max(res, get_score(i, j, data))
        # print(res, i, j)

print(res)
