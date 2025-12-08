import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2025
DAY = 6

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


dl = data.split("\n")
ll = dl[-1]
t = []
for l in dl[:-1]:
    t.append(nums(l))

lll = re.findall(r"[+*]", ll)
s = len(lll)
# print(s)
tt = []
for i in range(s):
    if lll[i] == "+":
        tt.append(0)
    else:
        tt.append(1)
    for j in range(len(t)):
        if lll[i] == "+":
            tt[i] += t[j][i]
        else:
            tt[i] *= t[j][i]


print(sum(tt))

res = 0
# columns widths
widths = []

for i in range(s):  # columns
    ints = [elt[i] for elt in t]
    widths.append(max([len(str(i)) for i in ints]))

# print(widths)
idxs = [widths[0]]
for w in widths[1:]:
    idxs.append(idxs[-1] + 1 + w)
# print(idxs)

"""
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + 
"""

tt = []
data = as_grid(data)
# print(data)
for i in range(s):  # big columns
    ints = [elt[i] for elt in t]
    # print(ints)
    cond = lll[i] == "+"
    w = widths[i]
    idd = idxs[i]
    if cond:
        tt.append(0)
    else:
        tt.append(1)
    for sc in range(w):  # sub columns
        k = 0
        for j in range(len(t)):
            # print(idd - sc - 1, data[j], len(data[j]))
            if data[j][idd - sc - 1] == " " and k > 0:
                break
            if data[j][idd - sc - 1] == " " and k == 0:
                continue
            k *= 10
            k += int(data[j][idd - sc - 1])

        if cond:
            tt[i] += k
        else:
            tt[i] *= k
print(sum(tt))
