import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2025
DAY = 1

data = aoct.get_input(YEAR, DAY)

res = 0
res2 = 0
# graphs
# V = list(set(re.findall(r'[a-z]{2}', data)))
# V_T = {V[i] : i for i in range(len(V))}
# edges = [(V_T[a], V_T[b]) for a, b in re.findall(r'([a-z]{2})\-([a-z]{2})', data)]
# G = ig.Graph(edges=edges, directed=False)
# edges = [(V_T[a], V_T[b], int(c)) for a, b, c in re.findall(r'([a-z]{2})\-([a-z]{2})\-(\d+)', data)]
# G = ig.Graph(edges=[(s,t) for s,t,_ in edges], directed=False, edge_attrs={"weight": [w for _,_,w in edges]})

# data = as_grid(data)

# data = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82"""
o = 50
for l in data.split("\n"):
    r = nums(l)[0]
    prev = o
    if l[0] == "R":
        o += r
    if l[0] == "L":
        o -= r

    a = range(min(prev, o), max(prev, o) + 1)
    a = [e % 100 for e in a]
    if 0 in a:
        if o % 100 == 0:
            res += 1
        res2 += a.count(0)

        if prev == 0:
            res2 -= 1

    o %= 100


print(res, res2)
