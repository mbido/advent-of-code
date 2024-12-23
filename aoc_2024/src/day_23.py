import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 23

data = aoct.get_input(YEAR, DAY)

V = list(set(re.findall(r'[a-z]{2}', data)))
V_T = {V[i] : i for i in range(len(V))}

G = ig.Graph()
G.add_vertices(len(V))

edges = []
for l in data.split("\n"):
    a, b = l.split("-")
    edges.append((V_T[a], V_T[b]))

G.add_edges(edges)

cliques = G.cliques(min=3, max=3)

res = 0
for q in cliques:
    for e in q:
        if V[e][0] == "t":
            res += 1
            break

print(res)

LAN = max(G.cliques(), key=lambda e: len(e))
print(",".join(sorted([V[i] for i in LAN])))
