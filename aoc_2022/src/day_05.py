import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2022
DAY = 5

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
# print(data)

# data = """    [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2"""

pr, data = data.split("\n\n")
pr = pr.split("\n")[::-1]
N = max(nums(pr[0]))
C = [[] for _ in range(N)]

for l in pr[1:]:
    l = [l[i] for i in range(1, len(l), 4)]
    for i, c in enumerate(l):
        if c != " ":
            C[i].append(c)

for l in data.split("\n"):
    n, f, t = nums(l)
    temp = C[f - 1][-n:]
    C[f - 1] = C[f - 1][:-n]
    C[t - 1] += temp[::-1]


print("".join([l[-1] for l in C]))

C = [[] for _ in range(N)]

for l in pr[1:]:
    l = [l[i] for i in range(1, len(l), 4)]
    for i, c in enumerate(l):
        if c != " ":
            C[i].append(c)

for l in data.split("\n"):
    n, f, t = nums(l)
    temp = C[f - 1][-n:]
    C[f - 1] = C[f - 1][:-n]
    C[t - 1] += temp


print("".join([l[-1] for l in C]))