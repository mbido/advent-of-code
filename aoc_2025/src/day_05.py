import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2025
DAY = 5

data = aoct.get_input(YEAR, DAY)

res = 0

# graphs
# node_patern = r'[a-z]{2}'
# V = list(set(re.findall(node_patern, data)))
# V_T = {V[i] : i for i in range(len(V))}
# # Not directed
# edges = [(V_T[a], V_T[b]) for a, b in re.findall(r'(node_patern)\-(node_patern)', data)]
# G = ig.Graph(edges=edges, directed=False)
# # Directed
# edges = [(V_T[a], V_T[b], int(c)) for a, b, c in re.findall(r'(node_patern)\-(node_patern)\-(\d+)', data)]
# G = ig.Graph(edges=[(s,t) for s,t,_ in edges], directed=False, edge_attrs={"weight": [w for _,_,w in edges]})
# data = """3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32"""
# data = as_grid(data)
a, b = data.split("\n\n")
ranges = [nums(l) for l in a.split("\n")]
for l in b.split("\n"):
    l = nums(l)[0]
    for c, d in ranges:
        if c <= l <= d:
            res += 1
            break

print(res)


res = 0
nr = ranges.copy()
for i in range(len(ranges)):
    c, d = nr[i]
    for j in range(len(nr)):
        if j == i:
            continue
        e, f = nr[j]
        if e <= c <= d <= f:
            c = 0
            d = -1
        if e <= c <= f:
            c = f + 1
        elif e <= d <= f:
            d = e - 1

    # if c <= d:
    nr[i] = (c, d)

# |-----|
#  |--------|

# print(nr)
for c, d in nr:
    # print(c, d, d - c + 1)
    res += d - c + 1

print(res)
