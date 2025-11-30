import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2022
DAY = 2

data = aoct.get_input(YEAR, DAY)

res = 0

# graphs
# V = list(set(re.findall(r'[a-z]{2}', data)))
# V_T = {V[i] : i for i in range(len(V))}
# edges = [(V_T[a], V_T[b]) for a, b in re.findall(r'([a-z]{2})\-([a-z]{2})', data)]
# G = ig.Graph(edges=edges, directed=False)
# edges = [(V_T[a], V_T[b], int(c)) for a, b, c in re.findall(r'([a-z]{2})\-([a-z]{2})\-(\d+)', data)]
# G = ig.Graph(edges=[(s,t) for s,t,_ in edges], directed=False, edge_attrs={"weight": [w for _,_,w in edges]})

#data = as_grid(data)
p1 = ["A", "B", "C"]
p2 = ["X", "Y", "Z"]

for l in data.split("\n"):
    a, b = l.split(" ")
    ia = p1.index(a)
    ib = p2.index(b)
    res += ib + 1
    
    if ia == ib:
        res += 3
    elif ia == (ib - 1 ) % 3:
        res += 6


print(res)


res = 0
for l in data.split("\n"):
    a, b = l.split(" ")
    ia = p1.index(a)
    ib = p2.index(b)
    
    res += 1
    
    if ib == 0:
        res += (ia - 1) % 3
    elif ib == 1:
        res += ia + 3
    else:
        res += (ia + 1) % 3 + 6
        
        
print(res)