import hashlib
import re
import numpy as np
from itertools import product, permutations
from queue import PriorityQueue, Queue
from bisect import *
from functools import reduce, cmp_to_key
import matplotlib.pyplot as plt
import igraph as ig
import networkx as nx
import multiprocessing as mp
import z3
import heapq
import json
import math
import time
import copy
import random
import sys
import sympy
from pathlib import Path


sys.setrecursionlimit(10000000)

# ------ TUTORIALS -------

# iGraph :
# G.union(g2) <=>  g |= g2
# G.intersection(g2) <=> g and g2
# G.disjoint_union(g2)
# G.difference(g2)
# G.complementer()
# G.cliques()
# G.cliques(3) <=> G.cliques(min=3)
# G.cliques(max=3)
# G.cliques(min=3, max=3)
# G.largest_cliques()
# G.mincut(source=None, target=None, capacity=None) -> igraph.Cut -> cut_value ; partition ; crossing
# G.st_mincut(source, target, weights=None) -> cut.edges ; cut.cut_size ; cut.partition

# ------ Tools -------


adj4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
adj8 = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
alpha = "abcdefghijklmnopqrstuvwxyz"
alphA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
Alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def print_grid(grid):
    # prints a grid of chars
    for r in grid:
        for c in r:
            print(c, end="")
        print()
    print()


def as_grid(data, t=str):
    res = []
    for l in data.split("\n"):
        ll = list(l)
        print(res, ll, type(ll))
        res.append([t(c) for c in ll])
    return res


def as_lines(data):
    return data.split("\n")


def nums(string):
    return list(map(int, re.findall(r"(\d+)", string)))


def s_nums(string):
    return list(map(int, re.findall(r"([\-\+]?\d+)", string)))


def floats(string):
    return list(map(float, re.findall(r"(?:\d+(?:\.\d*)?|\.\d+)", string)))


def s_floats(string):
    return list(map(float, re.findall(r"[\-\+]?(?:\d+(?:\.\d*)?|\.\d+)", string)))


def md5(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def add_vertex_no_duplicate(g, vertex_name):
    try:
        g.vs.find(name=vertex_name)
        return False
    except ValueError:
        g.add_vertex(vertex_name)
        return True


def get_path_weight(g: ig.Graph, vList):
    weight = 0
    for i in range(len(vList) - 1):
        edge = g.get_eid(vList[i], vList[i + 1], error=False)
        if edge == -1:
            return -1
        weight += int(g.es[edge]["weight"])
    return weight


def int_lines(string: str):
    return [int(elt) for elt in string.split("\n")]


def get_grid(pos, grid, default="?"):
    y, x = pos
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        return grid[y][x]
    return default


def set_grid(pos, grid, value):
    y, x = pos
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        grid[y][x] = value
        return True
    return False


def find_in_grid(e, grid):
    for y, r in enumerate(grid):
        for x, c in enumerate(r):
            if c == e:
                return (y, x)
    return False


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def mp_for_sum(func, params, n_proc=8):
    def helper_mp_for_sum(func_and_params):
        func, params = func_and_params
        return sum(func(p) for p in params)

    n = len(params)
    chunksize = (n + n_proc - 1) // n_proc

    jobs = [(func, params[i : i + chunksize]) for i in range(0, n, chunksize)]

    with mp.Pool(n_proc) as pool:
        results = pool.imap_unordered(helper_mp_for_sum, jobs, chunksize=1)
        return sum(results)


def berlekamp_massey(sequence):
    n = len(sequence)
    c = [1] + [0] * n
    b = [1] + [0] * n
    L = 0
    m = -1
    delta = 0

    for i in range(n):
        delta = sequence[i]
        for j in range(1, L + 1):
            delta += c[j] * sequence[i - j]
        if delta != 0:
            t = c.copy()
            coef = delta / b[0]
            for j in range(len(b)):
                if i - m + j < len(c):
                    c[i - m + j] -= coef * b[j]
            if 2 * L <= i:
                L = i + 1 - L
                m = i
                b = t
    return c[: L + 1]


def next_term(relation, previous_terms):
    next_value = 0
    for coef, term in zip(
        relation[1:], reversed(previous_terms[-(len(relation) - 1) :])
    ):
        next_value -= coef * term
    return next_value


def get_divisors(n):
    p_factors = sympy.factorint(n)
    ps = sorted(p_factors.keys())
    omega = len(ps)

    exponents = [p_factors[p] for p in ps]

    def rec_gen(n=0):
        if n == omega:
            yield 1

        else:
            current_prime = ps[n]
            current_exponent = exponents[n]

            pows = [current_prime**i for i in range(current_exponent + 1)]

            for q in rec_gen(n + 1):
                for p in pows:
                    yield p * q

    return list(rec_gen())


def str2dig(string: str) -> int:
    """Give the digit corresponding to the start of the string -1 if not found:

    Examples:
        str2dig("ninesdfkdji") -> 9
        str2dig("kninekqsdfj") -> -1
    """
    str2dig_dict: dict = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for keys in str2dig_dict:
        if string[: len(keys)] == keys:
            return str2dig_dict[keys]
    return -1


def get_path_dict(paths: list[str | Path]) -> dict:
    """Builds a tree like structure out of a list of paths"""

    def _recurse(dic: dict, chain: tuple[str, ...] | list[str]):
        if len(chain) == 0:
            return
        if len(chain) == 1:
            dic[chain[0]] = None
            return
        key, *new_chain = chain
        if key not in dic:
            dic[key] = {}
        _recurse(dic[key], new_chain)
        return

    new_path_dict = {}
    for path in paths:
        _recurse(new_path_dict, Path(path).parts)
    return new_path_dict


if __name__ == "__main__":
    print("Starting tests...")
    print(floats("76-87 678sd3.4"))
    print(s_floats("76-87 678sd3.4"))
    print(s_nums("76-87 678sd3.4"))
    print(nums("76-87 678sd3.4"))
    # print(re.findall(r'(?:\d+(?:\.\d*)?|\.\d+)', "76S-87 678sd3.4"))
    # print(str2dig("nine"))
    # print(str2dig("knines"))
    #     data = """abcde
    # fghij"""
    #     print(as_grid(data))
    # print(s_nums("asd3, 1, 23sl9s-23"))
    # fib = berlekamp_massey([1, 1, 2, 3, 5, 8])
    # print(get_divisors(random.randint(10, 100000)))
