import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2022
DAY = 7

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


# data = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k"""

fs = {}
path = ["/"]

for l in data.split("\n")[1:]:
    content = l.split(" ")
    if len(content) == 3 and content[1] == "cd":
        if content[2] == "..":
            path = path[:-1]
        else:
            path.append(content[2] + "/")
        continue
    if len(content) == 2 and content[1] == "ls":
        continue

    if content[0] != "dir":
        key = "".join(path) + content[1]
        fs[key] = int(content[0])


def sizeof_dir(path, fs):
    res = 0
    for f in fs:
        if f.startswith(path):
            res += fs[f]
    return res


# print(sizeof_dir("", fs))
dirs = []
for path in fs:
    ld = path.split("/")[:-1]
    d = ""
    for elt in ld:
        d += elt + "/"
        dirs.append(d)

dirs = list(set(dirs))

print(sum([s for d in dirs if (s := sizeof_dir(d, fs)) <= 100000]))

dir_sizes = {d: sizeof_dir(d, fs) for d in dirs}
dirs.sort(key=lambda d: dir_sizes[d], reverse=True)

max_size = 70000000 - 30000000
current = dir_sizes["/"]
min_free = current - max_size

for d in dirs[::-1]:
    s = dir_sizes[d]
    if s > min_free:
        print(s)
        break
