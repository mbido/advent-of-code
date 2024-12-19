import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 16

data = aoct.get_input(YEAR, DAY)
# print(data)
res = 0

mfcsam = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""
m = {l.split(": ")[0] : int(l.split(": ")[1]) for l in mfcsam.split("\n")}

#data = as_grid(data)
for l in data.split("\n"):
    i, l = re.match(r'Sue (\d+)\: (.*)', l).groups()
    ml = {ll.split(": ")[0] : int(ll.split(": ")[1]) for ll in l.split(", ")}
    ok = True
    for k in ml:
        if ml[k] != m[k]:
            ok = False
            break
    if not ok :
        continue
    print(i)

for l in data.split("\n"):
    i, l = re.match(r'Sue (\d+)\: (.*)', l).groups()
    ml = {ll.split(": ")[0] : int(ll.split(": ")[1]) for ll in l.split(", ")}
    ok = True
    for k in ml:
        if k == "cats" or k == "trees":
            if ml[k] <= m[k]:
                ok = False
                break
        elif k == "pomeranians" or k == "goldfish":
            if ml[k] >= m[k]:
                ok = False
                break
        else :
            if ml[k] != m[k]:
                ok = False
                break
    if not ok :
        continue
    print(i)
