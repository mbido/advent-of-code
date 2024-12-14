import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 14

def move(px, py, vx, vy, X, Y):
    return (px + vx) % X,  (py + vy) % Y

def get_safety(grid):
    l1 = len(grid) // 2
    l2 = (len(grid[0])) // 2
    a = [row[:l2] for row in grid[:l1]]
    b = [row[:l2] for row in grid[l1+1:]]
    c = [row[l2+1:] for row in grid[:l1]]
    d = [row[l2+1:] for row in grid[l1+1:]]
    res = 1
    for g in [a, b, c, d]:
        r = 0
        for l in g:
            r += sum(l)
        res *= r
    return res

def pg(grid):
    for r in grid:
        for c in r:
            p = "#" if c > 0 else " "
            print(p, end="")
        print()
    print()

def part_1(data):
    X = 101
    Y = 103
    grid = [[0 for _ in range(X)] for _ in range(Y)]
    for l in data.split("\n"):
        px, py, vx, vy = list(map(int, re.findall(r'(\-?[0-9]+)', l)))
        
        for _ in range(100):
            px, py = move(px, py, vx, vy, X, Y)
        grid[py][px] += 1
        
    return get_safety(grid)

def get_score(grid, robots):
    res = 0
    for x, y, _, _ in robots:
        if get_grid(x + 1, y, grid, 0) > 0:
            res += 1
    return res

def part_2(data):
    
    X = 101
    Y = 103
    robots = []
    for l in data.split("\n"):
        rb = list(map(int, re.findall(r'(\-?[0-9]+)', l)))
        robots.append(rb)
        
    scores = []

    for i in range(1_000_000_000):
        g = [[0 for _ in range(X)] for _ in range(Y)]
        for r in robots:
            px, py, vx, vy = r
            r[0], r[1] = move(px, py, vx, vy, X, Y)
        for r in robots:
            px, py, _, _ = r
            g[py][px] += 1
        
        score = get_score(g, robots)
        if score / len(robots) > 0.5:
            pg(g)
            return i + 1
        scores.append(score)

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
