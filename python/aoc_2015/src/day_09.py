import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 9

line_re = re.compile(r"(\w+) to (\w+) = (\d+)")

def create_graph(data):
    g = ig.Graph()
    for line in data.split("\n"):
        c1, c2, dist = line_re.match(line).groups()
        add_vertex_no_duplicate(g, c1)
        add_vertex_no_duplicate(g, c2)
        g.add_edge(c1, c2, weight=dist)
    return g
        
def get_all_hamiltonian_sizes(g):
    vertices = [v["name"] for v in g.vs]
    res = []
    for p in permutations(vertices):
        w = get_path_weight(g, p)
        if w >= 0:
            res.append(w)
    return sorted(res)

global sizes
def part_1(data):
    global sizes
    g = create_graph(data)
    sizes = get_all_hamiltonian_sizes(g)
    return sizes[0] 

def part_2(data):
    return sizes[-1]

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
