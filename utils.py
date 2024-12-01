import hashlib
import re
import numpy as np
from itertools import product, permutations
import igraph as ig
import json
import math
from functools import reduce


def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def add_vertex_no_duplicate(g, vertex_name):
    try:
        g.vs.find(name=vertex_name)
        return False
    except ValueError:
        g.add_vertex(vertex_name)
        return True

def get_path_weight(g : ig.Graph, vList):
    weight = 0
    for i in range(len(vList) -1):
        edge = g.get_eid(vList[i], vList[i + 1], error=False)
        if edge == -1:
            return -1
        weight += int(g.es[edge]["weight"])
    return weight

def pgcd(values: list):
    return reduce(math.gcd, values)

def ppcm_pair(a: int, b:int):
    return abs(a * b) // math.gcd(a, b)

def ppcm(values: list):
    return reduce(ppcm_pair, values)