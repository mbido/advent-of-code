import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2025
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

# data = as_grid(data)
# for l in data.split("\n"):
#     l = nums(l)

# data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

ranges = [nums(p) for p in data.split(",")]
for a, b in ranges:
    for i in range(a, b + 1):
        si = str(i)
        l = len(si) // 2
        if si[:l] == si[l:]:
            res += i
print(res)


def parse_size_n(s, n):
    res = []
    for i in range((len(s) + n - 1) // n):
        res.append(s[i * n : (i + 1) * n])
    return res


res = 0
ranges = [nums(p) for p in data.split(",")]
for a, b in ranges:
    for i in range(a, b + 1):
        si = str(i)
        for l in range(1, len(si)):
            parsed = parse_size_n(si, l)
            b = [elt == parsed[0] for elt in parsed]
            if all(b):
                res += i
                break
print(res)
