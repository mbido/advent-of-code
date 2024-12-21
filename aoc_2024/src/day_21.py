import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 21

data = aoct.get_input(YEAR, DAY)

N = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["?", "0", "A"]
]

D = [
    ["?", "^", "A"],
    ["<", "v", ">"]
]

codes = data.split("\n")

def dir_to_char(dir):
    d = [
        ["?", "^", "?"],
        ["<", "?", ">"],
        ["?", "v", "?"]
    ]
    return d[dir[0] + 1][dir[1] + 1]

def get_path1(char, pos):
    p2 = find_in_grid(char, N)
    h = pos[1] - p2[1]
    v = pos[0] - p2[0]
    a = "<" * h if h > 0 else ">" * abs(h) 
    b = "^" * v if v > 0 else "v" * abs(v) 
    
    if a == "<" and pos == (3, 1) or a == "<<" and pos == (3, 2):
        return b + a + "A"
    
    if b == "v" and pos == (2, 0) or b == "vv" and pos == (1, 0) or b == "vvv" and pos == (0, 0):
        return a + b + "A"
    
    if a and a[0] == '>':
        return b + a + "A"
    return a + b + "A"

def get_path2(char, pos):
    p2 = find_in_grid(char, D)
    h = pos[1] - p2[1]
    v = pos[0] - p2[0]
    a = "<" * h if h > 0 else ">" * abs(h) 
    b = "^" * v if v > 0 else "v" * abs(v) 
    
    if a == "<" and pos == (0, 1) or a == "<<" and pos == (0, 2):
        return b + a + "A"
    
    if b == "^" and pos == (1, 0):
        return a + b + "A"
    
    if a and a[0] == '>':
        return b + a + "A"
    return a + b + "A"

cache = {}
def helper(code, depth):
    k = code + str(depth)
    if k in cache:
        return cache[k]
    
    if depth == 0:
        cache[k] = len(code)
        return len(code)
    
    res = 0
    last = find_in_grid("A", D)
    for char in code:
        p = get_path2(char, last)
        res += helper(p, depth - 1)
        last = find_in_grid(char, D)
    cache[k] = res
    return res

res = 0
for cd in codes:
    c = cd
    last = (3, 2)
    r = ""
    for char in c:
        r += get_path1(char, last)
        last = find_in_grid(char, N)
    c = r
    r = helper(c, 2)
    res += r * int(cd[:-1])
print(res)

res = 0
for cd in codes:
    c = cd
    last = (3, 2)
    r = ""
    for char in c:
        r += get_path1(char, last)
        last = find_in_grid(char, N)
    c = r
    r = helper(c, 25)
    res += r * int(cd[:-1])
print(res)