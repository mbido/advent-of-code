import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 18

def priority(pos, gn, end):
    return abs(pos[0] - end[0]) + abs(pos[1] - end[1]) + gn

def a_star(start, end, grid):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited[start[0]][start[1]] = 1
    heap = [(priority(start, 0, end), start)]
    p = (0, 0)
    while heap:
        y, x = heapq.heappop(heap)[1]
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
            heapq.heappush(heap, (priority(p, v + 1, end), p))
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
    return a_star(S, E, grid)[0]

def blocked(bt, R, grid, S, E):
    grid = [[(x, y) not in bt[:R] for x in range(len(grid[0]))] for y in range(len(grid))]
    return a_star(S, E, grid) == "ERROR"

def part_2(data):
    W = H = 71
    R = 1024
    
    bt = list(map(nums, data.split("\n")))
    grid = [[(x, y) not in bt[:R] for x in range(W)] for y in range(H)]
    
    S = (0, 0)
    E = (H - 1, W - 1)
    p = bisect_left(range(len(bt)), True, key=(lambda i: blocked(bt, i, grid, S, E)))
    return str(bt[p-1][0]) + "," + str(bt[p-1][1])

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
