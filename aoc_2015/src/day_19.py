import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
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

# s2 = "HOHOHO"

transforms = re.findall(r"([A-Z]?[a-z]?) \=\> ([A-Za-z]+)", s1)
tr = {}
for k, v in transforms:
    if not k in tr:
        tr[k] = [v]
    else:
        tr[k].append(v)


def transform_at(s, i, t):
    ml = re.findall(r"([A-Z][a-z]?)", s)
    tt = re.findall(r"([A-Z]?[a-z]?)", t)
    mlt = ml[:i] + tt + ml[i + 1 :]
    return "".join(mlt)


def get_all_1_trans(string, trans):
    ml = re.findall(r"([A-Z][a-z]?)", string)

    s = set()
    for i, a in enumerate(ml):
        if a not in trans:
            continue
        for t in trans[a]:
            s.add(transform_at(string, i, t))

    return s


def get_all_1_trans2(string, trans):
    s = set()
    for k in trans:
        matches = [(m.span(), m.group()) for m in re.finditer(re.escape(k), string)]
        for match in matches:
            bounds = match[0]
            for val in trans[k]:
                s.add(string[: bounds[0]] + val + string[bounds[1] :])
    return s


tr_e = tr["e"]
tr["e"] = []


def inverte_dict(base):
    res = {}
    for k, vs in base.items():
        for v in vs:
            if v not in res:
                res[v] = []
            res[v].append(k)
    return res


# NOT MY WORK  :
reps = transforms
mol = s2

target = mol
part2 = 0

t = 0
while target != "e":
    tmp = target
    for a, b in reps:
        if b not in target:
            continue

        target = target.replace(b, a, 1)
        part2 += 1

    if tmp == target:
        t += 1
        target = mol
        part2 = 0
        random.shuffle(reps)

print(part2)
