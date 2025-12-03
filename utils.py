import hashlib
import re
import numpy as np
import z3
import heapq
import json
import math
import time
import copy
import random
import sys
import sympy
import igraph as ig
import networkx as nx
from itertools import product, permutations
from queue import PriorityQueue, Queue
from bisect import *
from functools import reduce, cmp_to_key
import matplotlib.pyplot as plt
from pathlib import Path
from collections import deque
from typing import List, Tuple, Dict, Any, Union, Callable, Optional, Generator

sys.setrecursionlimit(100000000)

# ==============================================================================
# CONSTANTS
# ==============================================================================

adj4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
adj8 = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
alpha = "abcdefghijklmnopqrstuvwxyz"
alphA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
Alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# ==============================================================================
# GRAPHS (IGRAPH)
# ==============================================================================


# g.union(g2) <=> g |= g2
# g.intersection(g2) <=> g and g2
# g.disjoint_union(g2)
# g.difference(g2)
# g.complementer()
# g.cliques()
# g.cliques(3) <=> g.cliques(min=3)
# g.cliques(max=3)
# g.cliques(min=3, max=3)
# g.largest_cliques()
# g.mincut(source=None, target=None, capacity=None) -> igraph.Cut -> cut_value ; partition ; crossing
# g.st_mincut(source, target, weights=None) -> cut.edges ; cut.cut_size ; cut.partition
# g.distances(source, target, weights=...)
# g.get_shortest_paths(v, to=..., weights=..., output="vpath")
# g.get_all_shortest_paths(v, to=..., weights=..., output="vpath")
# g.simplify()
# g.spanning_tree(weights=...)
# g.degree(u, mod="...") -> mod in {"in", "out"}
# g.topological_sorting(mode="...")


def add_vertex_no_duplicate(g: ig.Graph, vertex_name: str) -> bool:
    """Ajoute un sommet au graphe igraph seulement s'il n'existe pas déjà (par nom)."""
    try:
        g.vs.find(name=vertex_name)
        return False
    except ValueError:
        g.add_vertex(vertex_name)
        return True


def get_path_weight(g: ig.Graph, vList: List[Any]) -> int:
    """Calcule le poids total d'un chemin défini par une liste de sommets."""
    weight = 0
    for i in range(len(vList) - 1):
        edge = g.get_eid(vList[i], vList[i + 1], error=False)
        if edge == -1:
            return -1
        weight += int(g.es[edge]["weight"])
    return weight


# ==============================================================================
# PARSING & STRING MANIPULATION
# ==============================================================================


def as_lines(data: str) -> List[str]:
    """Sépare une chaîne de caractères par sauts de ligne."""
    return data.split("\n")


def int_lines(string: str) -> List[int]:
    """Convertit une chaîne multi-lignes en liste d'entiers (un par ligne)."""
    return [int(elt) for elt in string.split("\n")]


def nums(string: str) -> List[int]:
    """Extrait tous les nombres entiers positifs d'une chaîne."""
    return list(map(int, re.findall(r"(\d+)", string)))


def s_nums(string: str) -> List[int]:
    """Extrait tous les nombres entiers (positifs et négatifs) d'une chaîne."""
    return list(map(int, re.findall(r"([\-\+]?\d+)", string)))


def floats(string: str) -> List[float]:
    """Extrait tous les nombres à virgule positifs d'une chaîne."""
    return list(map(float, re.findall(r"(?:\d+(?:\.\d*)?|\.\d+)", string)))


def s_floats(string: str) -> List[float]:
    """Extrait tous les nombres à virgule (positifs et négatifs) d'une chaîne."""
    return list(map(float, re.findall(r"[\-\+]?(?:\d+(?:\.\d*)?|\.\d+)", string)))


def str2dig(string: str) -> int:
    """Convertit le nom d'un chiffre (anglais) en début de chaîne en entier (-1 si non trouvé)."""
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


def md5(s: str) -> str:
    """Retourne le hash MD5 hexadécimal d'une chaîne UTF-8."""
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def get_path_dict(paths: List[Union[str, Path]]) -> Dict[str, Any]:
    """Construit une structure arborescente (dictionnaire imbriqué) à partir d'une liste de chemins."""

    def _recurse(dic: dict, chain: Union[Tuple[str, ...], List[str]]):
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


# ==============================================================================
# GRIDS & 2D GEOMETRY
# ==============================================================================


def print_grid(grid: List[List[Any]]) -> None:
    """Affiche une grille 2D ligne par ligne dans la console."""
    for r in grid:
        for c in r:
            print(c, end="")
        print()
    print()


def as_grid(data: str, t: Callable = str) -> List[List[Any]]:
    """Convertit une chaîne brute en grille 2D en appliquant le type t à chaque cellule."""
    return [list(map(t, line)) for line in data.splitlines()]


def get_grid(pos: Tuple[int, int], grid: List[List[Any]], default: Any = "?") -> Any:
    """Récupère la valeur d'une cellule (y, x) ou une valeur par défaut si hors limites."""
    y, x = pos
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        return grid[y][x]
    return default


def set_grid(pos: Tuple[int, int], grid: List[List[Any]], value: Any) -> bool:
    """Modifie la valeur d'une cellule (y, x) si les coordonnées sont valides."""
    y, x = pos
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        grid[y][x] = value
        return True
    return False


def find_in_grid(e: Any, grid: List[List[Any]]) -> Union[Tuple[int, int], bool]:
    """Retourne les coordonnées (y, x) de la première occurrence de l'élément e, ou False."""
    for y, r in enumerate(grid):
        for x, c in enumerate(r):
            if c == e:
                return (y, x)
    return False


def manhattan(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    """Calcule la distance de Manhattan entre deux points (y, x)."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def bfs(
    grid: List[List[Any]],
    start: Tuple[int, int],
    walls: str = "#",
    neighbours: List[Tuple[int, int]] = adj4,
    objective=None,
) -> Dict[Tuple[int, int], int]:
    """Effectue un parcours en largeur (BFS) et retourne un dictionnaire {pos: distance}."""
    queue = deque([(start, 0)])
    visited = {start: 0}

    if type(objective) == Tuple and start == objective:
        return visited

    while queue:
        (y, x), dist = queue.popleft()

        for dy, dx in neighbours:
            ny, nx = y + dy, x + dx
            npos = (ny, nx)

            cell_value = get_grid(npos, grid, default=walls[0])
            if cell_value in walls:
                continue

            if npos in visited:
                continue

            if type(objective) == str and cell_value == objective:
                return visited

            visited[npos] = dist + 1
            queue.append((npos, dist + 1))

    return visited


# ==============================================================================
# MATH & SEQUENCES
# ==============================================================================


def berlekamp_massey(sequence: List[Union[int, float]]) -> List[Union[int, float]]:
    """Trouve le polynôme générateur minimal pour une suite linéaire récurrente."""
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


def next_term(
    relation: List[Union[int, float]], previous_terms: List[Union[int, float]]
) -> Union[int, float]:
    """Calcule le terme suivant d'une suite en utilisant sa relation de récurrence."""
    next_value = 0
    for coef, term in zip(
        relation[1:], reversed(previous_terms[-(len(relation) - 1) :])
    ):
        next_value -= coef * term
    return next_value


def get_divisors(n: int) -> List[int]:
    """Génère la liste de tous les diviseurs d'un entier n."""
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


# ==============================================================================
# MAIN / TESTS
# ==============================================================================

if __name__ == "__main__":
    print("Starting tests...")
    print(floats("76-87 678sd3.4"))
    print(s_floats("76-87 678sd3.4"))
    print(s_nums("76-87 678sd3.4"))
    print(nums("76-87 678sd3.4"))
