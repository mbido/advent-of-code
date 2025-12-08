import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2025
DAY = 7

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

# data = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ..............."""

data = as_grid(data)
start = find_in_grid("S", data)
splitters = set()
jc = set([start[1]])
for i in range(len(data)):
    new_jc = set()
    for c in jc:
        if get_grid((i, c), data) == "^":
            splitters.add((i, c))
            new_jc.add(c - 1)
            new_jc.add(c + 1)
        else:
            new_jc.add(c)

    jc = new_jc

print(len(splitters))


def add_to_dict(a, d, times):
    if a not in d:
        d[a] = 1 * times
    else:
        d[a] += 1 * times


jc = {start[1]: 1}

for i in range(len(data)):
    new_jc = {}
    for c in jc:
        if get_grid((i, c), data) == "^":
            add_to_dict(c - 1, new_jc, jc[c])
            add_to_dict(c + 1, new_jc, jc[c])
        else:
            add_to_dict(c, new_jc, jc[c])
    jc = new_jc

print(sum([jc[i] for i in jc]))
# print(splitters)
