import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 19

data = aoct.get_input(YEAR, DAY)
# print(data)
s1, s2 = data.split("\n\n")

# s1 = """e => H
# e => O
# H => HO
# H => OH
# O => HH"""

# s2 = "HOH"

transforms = re.findall(r'([A-Z]?[a-z]?) \=\> ([A-Za-z]+)', s1)
tr = {}
for k, v in transforms:
    if not k in tr:
        tr[k] = [v]
    else:
        tr[k].append(v)
        
ml = re.findall(r'([A-Z][a-z]?)', s2)

s = set()
for i, a in enumerate(ml):
    if a not in tr:
        continue
    for t in tr[a]:
        tt = re.findall(r'([A-Z][a-z]?)', t)
        mlt = ml[:i] + tt + ml[i + 1:]
        s.add("".join(mlt))

print(len(s))

rvt = {}
for k, v in tr.items():
    for e in v:
        if e not in rvt:
            rvt[e] = [k]
        else:
            rvt[e].append(k)
print(rvt)

# cache = {}
# def go_to_e(rvt, ml):
#     if ml == "e":
#         return 0
#     for i, a in enumerate(ml):
#         if a not in rvt:
#             continue
#         for t in rvt[a]:
#             tt = re.findall(r'([A-Z][a-z]?)', t)
#             mlt = ml[:i] + tt + ml[i + 1:]
