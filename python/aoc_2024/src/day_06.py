import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 6

def find_pos(grid):
    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if c == "^":
                return [i, j]
    return "ERROR"

def get_front(pos, dir, grid):
    dirs = [[-1, 0],[0, 1], [1, 0], [0, -1]]
    return get_grid(pos[1] + dirs[dir][1], pos[0] + dirs[dir][0], grid)

def print_grid(grid):
    for r in grid:
        p = ""
        for c in r:
            p += c
        print(p)
    print()


def part_1(data):
    grid = [list(r) for r in data.split("\n")]
    pos = find_pos(grid)
    dir = 0
    dirs = [[-1, 0],[0, 1], [1, 0], [0, -1]]
    front = get_front(pos, dir, grid)
    while front != "?":
        grid[pos[0]][pos[1]] = "X"
        if front == "#":
            dir = (dir + 1) % 4
        else:
            pos = [pos[0] + dirs[dir][0], pos[1] + dirs[dir][1]]
        front = get_front(pos, dir, grid)
    grid[pos[0]][pos[1]] = "X"
    res = 0
    for r in grid:
        res += r.count("X")
    return res

def is_looping(grid, pos):
    dir = 0
    dirs = [[-1, 0],[0, 1], [1, 0], [0, -1]]
    front = get_front(pos, dir, grid)
    path = set()
    while front != "?":
        # grid[pos[0]][pos[1]] = "X"
        k = str(pos) + str(dir)
        if k in path:
            return True
        path.add(k)
        if front == "#":
            dir = (dir + 1) % 4
        else:
            pos = [pos[0] + dirs[dir][0], pos[1] + dirs[dir][1]]
        front = get_front(pos, dir, grid)
    return False
    

def part_2_old(data):
    grid = [list(r) for r in data.split("\n")]
    pos = find_pos(grid)
    res = 0
    for y in range(len(data.split("\n"))):
        for x in range(len(data.split("\n")[0])):
            
            g = [list(r) for r in data.split("\n")]
            if pos == [y, x] or g[y][x] == "#":
                continue
            g[y][x] = "#"
            
            if is_looping(g, pos):
                res += 1
    return res

def for_x(params):
    res = 0
    data, pos, y = params
    for x in range(len(data.split("\n")[0])):
        g = [list(r) for r in data.split("\n")]
        if pos == [y, x] or g[y][x] == "#":
            continue
        g[y][x] = "#"
            
        if is_looping(g, pos):
            res += 1
    return res

def part_2(data):
    grid = [list(r) for r in data.split("\n")]
    pos = find_pos(grid)
    return mp_for_sum(for_x, [[data, pos, y] for y in range(len(data.split("\n")))])

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    start_time = time.time()
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
    end_time = time.time()
    print(f'Time taken : {end_time - start_time} seconds')
