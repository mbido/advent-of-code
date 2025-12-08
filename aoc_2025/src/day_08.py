import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2025
DAY = 8

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

# data = """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689"""


# data = as_grid(data)

coords = []
for l in data.split("\n"):
    x, y, z = nums(l)
    coords.append((x, y, z))

pairs = [(a, b) for i, a in enumerate(coords) for b in coords[i + 1 :]]
pairs.sort(key=lambda x: e_dist(x[0], x[1]))
# print(pairs)

edges = [(str(a), str(b)) for a, b in pairs[:1000]]
G = ig.Graph.TupleList(edges, directed=False)
g = G.decompose()

l = sorted([len(e.vs) for e in g], reverse=True)
print(l[0] * l[1] * l[2])


edges = [(str(a), str(b), e_dist(a, b)) for a, b in pairs]
G = ig.Graph.TupleList(edges, directed=False, edge_attrs="weight")

mst = G.spanning_tree(weights="weight")
last_edge = max(mst.es, key=lambda e: e["weight"])

p1, p2 = eval(mst.vs[last_edge.source]["name"]), eval(mst.vs[last_edge.target]["name"])
print(p1[0] * p2[0])
