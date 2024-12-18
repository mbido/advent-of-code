import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 18

def show(grid, visited):
    for y, l in enumerate(grid):
        for x, c in enumerate(l):
            w = get_grid(x, y, visited, 10**20)
            if w != False:
                print("O", end="")
            elif c:
                print(" ", end="")
            else:
                print("#", end="")
        print()
    print()

def show_path(p, grid, visited):
    res = []
    path = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    while p != (0, 0):
        res.append(p)
        path[p[0]][p[1]] = True
        v = visited[p[0]][p[1]]
        p2 = p
        v2 = v
        for y, x in adj4:
            if not get_grid(p[1] + x, p[0] + y, grid, False):
                continue
            v3 = visited[p[0] + y][p[1] + x]
            if v3 < v2:
                v2 = v3
                p2 = (p[0] + y, p[1] + x)
        p = p2
    show(grid, path)
    return res

def bfs(start, end, grid):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    q = Queue()
    visited[start[0]][start[1]] = 1
    q.put(start)
    p = (0, 0)
    while not q.empty():
        y, x = q.get()
        p = (y, x)
        v = get_grid(x, y, visited, False)
        if (y, x) == end:
            return v - 1, visited
        
        for yi, xi in adj4:
            p = (y + yi, x + xi)
            v2 = get_grid(p[1], p[0], visited, False)
            if not get_grid(p[1], p[0], grid, False) or v2 != False:
                continue
            visited[p[0]][p[1]] = v + 1
            q.put(p)
    return "ERROR"

def part_1(data):
    W = H = 71
    R = 1024
    grid = [[True for _ in range(W)] for _ in range(H)]
    data = data.split("\n")
    for i in range(R):
        x, y = nums(data[i])
        grid[y][x] = False

    S = (0, 0)
    E = (H - 1, W - 1)
    return bfs(S, E, grid)[0]

def blocked(bt, R, grid, S, E):
    grid = copy.deepcopy(grid)
    for x, y in bt[:R]:
        grid[y][x] = False
    if bfs(S, E, grid) == "ERROR":
        return True
    return False

def part_2(data):
    W = H = 71
    R = 1024
    
    bt = list(map(nums, data.split("\n")))
    grid = [[True for _ in range(W)] for _ in range(H)]
    for x, y in bt[:R]:
        grid[y][x] = False
    
    S = (0, 0)
    E = (H - 1, W - 1)
    p = bisect_left(range(len(bt)), True, key=(lambda i: int(blocked(bt, i, grid, S, E))))
    print(p, bt[p])
    return str(bt[p-1][0]) + "," + str(bt[p-1][1])

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
