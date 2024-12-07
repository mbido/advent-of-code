import hashlib
import re
import numpy as np
from itertools import product, permutations
import igraph as ig
import json
import math
from functools import reduce, cmp_to_key
import multiprocessing as mp
import time

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

def int_lines(string : str):
    return [int(elt) for elt in string.split("\n")]

def get_grid(x, y, grid, default="?"):
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        return grid[y][x]
    return default

def helper_mp_for_sum(func_and_params):
    func, params = func_and_params
    return sum(func(p) for p in params)

def mp_for_sum(func, params, n_proc=8):
    n = len(params)
    chunksize = (n + n_proc - 1) // n_proc 

    jobs = [(func, params[i:i + chunksize]) for i in range(0, n, chunksize)]

    with mp.Pool(n_proc) as pool: 
        results = pool.imap_unordered(helper_mp_for_sum, jobs, chunksize=1)
        return sum(results)