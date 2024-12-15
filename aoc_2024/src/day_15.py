import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 15

def find_robot(grid):
    p = (0, 0)
    for j, l in enumerate(grid):
        for i, c in enumerate(l):
            if c == "@":
                p = (j, i)
                return p
    return "ERROR"

def move(p, dir, grid):
    p2 = (p[0] + dir[0], p[1] + dir[1])
    front = get_grid(p2[1], p2[0], grid)
    boxe = False
    while front == "O":
        boxe = True
        p2 = (p2[0] + dir[0], p2[1] + dir[1])
        front = get_grid(p2[1], p2[0], grid)
    if front == "#":
        return p
    grid[p[0]][p[1]] = "."
    grid[p[0] + dir[0]][p[1] + dir[1]] = "@"
    if boxe:
        grid[p2[0]][p2[1]] = "O"
    return (p[0] + dir[0], p[1] + dir[1])

def part_1(data):
    s1, s2 = data.split("\n\n")
    s2 = "".join(s2.split("\n"))
    grid = as_grid(s1)
    p = find_robot(grid)
    dirs = ["^", ">", "v", "<"]
    for d in s2:
        i = dirs.index(d)
        p = move(p, adj4[i], grid)
    res = 0
    for j, l in enumerate(grid):
        for i, c in enumerate(l):
            if c == "O":
                res += 100 * j + i
    
    return res

def transform(grid):
    res = [[] for _ in grid]
    for j, l in enumerate(grid):
        for c in l:
            if c == "#":
                res[j] += ["#", "#"]
            elif c == ".":
                res[j] += [".", "."]
            elif c == "O":
                res[j] += ["[", "]"]
            elif c == "@":
                res[j] += ["@", "."]
    return res

def move2_EO(p, dir, grid):
    # dir = ">" or "<"
    p2 = (p[0] + dir[0], p[1] + dir[1])
    front = get_grid(p2[1], p2[0], grid)
    boxe = False
    
    while front == "[" or front == "]":
        boxe = True
        p2 = (p2[0] + dir[0], p2[1] + dir[1])
        front = get_grid(p2[1], p2[0], grid)
        
    if front == "#":
        return p
    
    if boxe:
        p2 = (p[0] + dir[0], p[1] + dir[1])
        front = get_grid(p2[1], p2[0], grid)
        while front == "[" or front == "]":
            
            grid[p2[0]][p2[1]] = "]" if front == "[" else "["
            p2 = (p2[0] + dir[0], p2[1] + dir[1])
            front = get_grid(p2[1], p2[0], grid)
            
        grid[p2[0]][p2[1]] = "[" if dir == adj4[3] else "]"
    
    grid[p[0]][p[1]] = "."
    grid[p[0] + dir[0]][p[1] + dir[1]] = "@"
    
    return (p[0] + dir[0], p[1] + dir[1])

def push_boxe(pos, dir, g_copy):
    # pos is the position of the "[" of the boxe
    fp = (pos[0] + dir[0], pos[1] + dir[1])
    fl = g_copy[fp[0]][fp[1]]
    fr = g_copy[fp[0]][fp[1] + 1]
    
    if fl == "#" or fr == "#":
        return False, g_copy
    
    if fl == "." and fr == ".":
        g_copy[fp[0]][fp[1]] = "["
        g_copy[fp[0]][fp[1] + 1] = "]"
        g_copy[pos[0]][pos[1]] = "."
        g_copy[pos[0]][pos[1] + 1] = "."
        return True, g_copy
    
    a = b = "ERROR"

    if fl == "[" or fl == "]":
        fpl = fp if fl == "[" else (fp[0], fp[1] - 1)
        a, g_copy = push_boxe(fpl, dir, g_copy)
    if fr == "[": # don't check for fr == "]"
        fpl = (fp[0], fp[1] + 1)
        b, g_copy = push_boxe(fpl, dir, g_copy)
        
    if a and b:
        g_copy[fp[0]][fp[1]] = "["
        g_copy[fp[0]][fp[1] + 1] = "]"
        g_copy[pos[0]][pos[1]] = "."
        g_copy[pos[0]][pos[1] + 1] = "."
        return True, g_copy
    return False, g_copy

def move2_NS(p, dir, grid):
    # dir = "^" or "v"
    fp = (p[0] + dir[0], p[1] + dir[1])
    front = get_grid(fp[1], fp[0], grid)
    
    if front == "#":
        return p
    
    if front == "[" or front == "]":
        g_copy = copy.deepcopy(grid)
        pb = fp if front == "[" else (fp[0], fp[1] - 1)
        ok, g_copy = push_boxe(pb, dir, g_copy)
        if ok :
            grid[:] = g_copy[:]
            grid[p[0]][p[1]] = "."
            grid[p[0] + dir[0]][p[1] + dir[1]] = "@"
            return (p[0] + dir[0], p[1] + dir[1])
        return p
    
    grid[p[0]][p[1]] = "."
    grid[p[0] + dir[0]][p[1] + dir[1]] = "@"
    return (p[0] + dir[0], p[1] + dir[1])
    

def part_2(data):
    s1, s2 = data.split("\n\n")
    s2 = "".join(s2.split("\n"))
    grid = transform(as_grid(s1))
    p = find_robot(grid)
    dirs = ["^", ">", "v", "<"]
    for d in s2:
        i = dirs.index(d)
        if i % 2 == 0:
            p = move2_NS(p, adj4[i], grid)
        else:
            p = move2_EO(p, adj4[i], grid)
    res = 0
    for j, l in enumerate(grid):
        for i, c in enumerate(l):
            if c == "[":
                res += 100 * j + i
    print_grid(grid)
    return res

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
