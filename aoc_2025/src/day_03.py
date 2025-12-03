import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2025
DAY = 3

data = aoct.get_input(YEAR, DAY)

res = 0

# # Graphs (iGraph)
# node_pattern = r'[a-z]{2}' # ex: AA, zz
# # node_pattern = r'\d+'      # ex: 0, 42
#
# # 1. Simple
# edges = re.findall(f"({node_pattern})-({node_pattern})", data)
# G = ig.Graph.TupleList(edges, directed=False)
#
# # 2. Weighted
# raw_edges = re.findall(f"({node_pattern})-({node_pattern})-(\d+)", data)
# edges = [(u, v, int(w)) for u, v, w in raw_edges]
# G = ig.Graph.TupleList(edges, directed=False, edge_attrs="weight")
#
# # Utils
# # map_v = {v["name"]: v.index for v in G.vs}

# data = as_grid(data)
for l in data.split("\n"):
    maxi = 0
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if int(l[i] + l[j]) > maxi:
                maxi = int(l[i] + l[j])
    res += maxi

print(res)

# data = data[:20]


def jol(n, s, current):
    if n == 0:
        return current
    res = current
    maxi = int(current)
    idx = 0
    for i in range(len(s) - n + 1):
        new = current + s[i]
        if int(new) > maxi:
            maxi = int(new)
            idx = i
            res = new
    return jol(n - 1, s[idx + 1 :], res)


def jol2(s):
    sl = [int(elt) for elt in list(s)]
    start = 0
    res = 0

    for i in range(12, 0, -1):
        current_list = sl[start : -(i - 1)] if i != 1 else sl[start:]
        m = max(current_list)
        start = start + current_list.index(m) + 1
        res *= 10
        res += m

    return res


res = 0
res2 = 0

for l in data.split("\n"):
    k = jol(12, l, "0")
    res += int(k)
    res2 += jol2(l)
print(res)
print(res2)
