import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2025
DAY = 9

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

# data = as_grid(data)


# data = """7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3"""
c = []
for l in data.split("\n"):
    l = nums(l)
    c.append(tuple(l))


ma = 0
for p1, p2 in combinations(c, 2):
    a = abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1)
    ma = max(ma, a)


print(ma)

poly = Polygon(c)

for p1, p2 in combinations(c, 2):
    mi1, mi2 = sorted((p1[0], p2[0]))
    mj1, mj2 = sorted((p1[1], p2[1]))

    a = (mi2 - mi1 + 1) * (mj2 - mj1 + 1)

    if a <= ma:
        continue

    r = box(mi1, mj1, mi2, mj2)

    if poly.contains(r):
        ma = a

print(ma)
