import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2025
DAY = 4

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
# data = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@."""
data = as_grid(data)
for i in range(len(data)):
    for j in range(len(data[0])):
        if [get_grid((i + di, j + dj), data) for di, dj in adj8].count(
            "@"
        ) < 4 and get_grid((i, j), data) == "@":
            res += 1

print(res)

res = 0
to_check = [(i, j) for i in range(len(data)) for j in range(len(data[0]))]
while len(to_check) > 0:
    i, j = to_check.pop()
    ad = [(i + di, j + dj) for di, dj in adj8]
    if [get_grid((k, l), data) for k, l in ad].count("@") < 4 and get_grid(
        (i, j), data
    ) == "@":
        res += 1
        set_grid((i, j), data, "?")
        to_check += ad

print(res)
