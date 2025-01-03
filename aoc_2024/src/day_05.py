import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 5

def is_in_order(pages, order):
    r = []
    for p in pages:
        if p in order:
            for b in order[p]:
                if b in pages and b not in r:
                    return False
            r.append(p)
        else:
            r.append(p)
    return True

def part_1(data):
    O, U = data.split("\n\n")
    U = U.split()
    order = {}
    for l in O.split():
        v, k = l.split("|")
        if k in order:
            order[k].append(v)
        else:
            order[k] = [v]
    
    res = 0
    for u in U:
        u = u.split(",")
        if is_in_order(u, order):
            res += int(u[len(u) // 2])
    return res

def in_order(pages, order):
    r = []
    for i, p in enumerate(pages):
        if p in order:
            for b in order[p]:
                if b in pages and b not in r:
                    # REORDER
                    pages.remove(b)
                    pages = pages[:i] + [b] + pages[i:]
                    return in_order(pages, order)
            r.append(p)
        else:
            r.append(p)
    return pages

def part_2(data):
    O, U = data.split("\n\n")
    U = U.split()
    order = {}
    for l in O.split():
        v, k = l.split("|")
        if k in order:
            order[k].append(v)
        else:
            order[k] = [v]
    
    res = 0
    for u in U:
        u = u.split(",")
        if not is_in_order(u, order):
            u = in_order(u, order)
            res += int(u[len(u) // 2])
    return res

def part_1_and_2(data):

    rules, pages = data.split("\n\n")
    # x dois se trouver avant y si il existe la regle x|y => la clé doit renvoyer -1
    cmp = cmp_to_key(lambda x, y: -(x+'|'+y in rules))

    a = [0, 0]
    for p in pages.split():
        p = p.split(',')
        s = sorted(p, key=cmp)
        a[p!=s] += int(s[len(s)//2])

    return a

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
    aoct.submit_answer(YEAR, DAY, part_1_and_2(data), level=2, send=False)
