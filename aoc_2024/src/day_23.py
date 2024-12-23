import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 23

data = aoct.get_input(YEAR, DAY)

# graphs
V = list(set(re.findall(r'[a-z]{2}', data)))
V_T = {V[i] : i for i in range(len(V))}
edges = [(V_T[a], V_T[b]) for a, b in re.findall(r'([a-z]{2})\-([a-z]{2})', data)]
G = ig.Graph(edges=edges, directed=False)

print(len([c for c in G.cliques(min=3, max=3) if any(V[e].startswith("t") for e in c)]))
print(",".join(sorted([V[i] for i in max(G.cliques(), key=lambda e: len(e))])))