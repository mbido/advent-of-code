import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2024
DAY = 16

def djikstra(pos, dir, grid, scores, end):
    if pos == end:
        return scores
    score = scores[pos[0]][pos[1]]
    id = adj4.index(dir)
    for i in range(4):
        dd = adj4[(id - i + 4) % 4]
        s = 1 if i == 0 else 1001
        s += score[0]
        front = get_grid(pos[1] + dd[1], pos[0] + dd[0], grid, "#")
        if front == "#":
            continue
        front_s = get_grid(pos[1] + dd[1], pos[0] + dd[0], scores, False)
        if s < front_s[0]:
            scores[pos[0] + dd[0]][pos[1] + dd[1]] = (s, pos)
            scores = djikstra((pos[0] + dd[0], pos[1] + dd[1]), dd, grid, scores, end)
    return scores

def print_scores(scores):
    for y, l in enumerate(scores):
        for x, c in enumerate(l):
            if c[0] == 10**20:
                print(" ", end="")
            else:
                d = ""
                if c[1] == (y, x - 1):
                    d = ">"
                elif c[1] == (y, x + 1):
                    d = "<"
                elif c[1] == (y - 1, x):
                    d = "^"
                elif c[1] == (y + 1, x):
                    d = "v"
                print(d, end="")
        print()

def part_1(data):
    data = as_grid(data)
    scores = [[(10**20, (-1, -1)) for _ in l] for l in data]
    S = (len(data) - 2, 1)
    E = (1, len(data[0]) - 2)
    scores[S[0]][S[1]] = (0, (0, 0))
    scores = djikstra(S, (0, 1), data, scores, E)
    return scores[E[0]][E[1]][0]

def get_tiles(pos, scores, visited, dir, S):
    if pos in visited or pos == S:
        return visited
    visited.add(pos)
    best = 10**20
    best_pos = []
    best_d = []
    for d in adj4:
        p = (pos[0] + d[0], pos[1] + d[1])
        s = scores[p[0]][p[1]][0]
        if d != dir:
            s += 1000
        
        if s < best:
            best_pos = [p]
            best_d = [d]
            best = s
        elif s == best:
            best_pos.append(p)
            best_d.append(d)
    for i, p in enumerate(best_pos):
        visited = get_tiles(p, scores, visited, best_d[i], S)
    return visited

def print_pos(visited, grid):
    for y, r in enumerate(grid):
        for x, c in enumerate(r):
            if (y, x) in visited:
                print("O", end="")
            else:
                print(c, end="")
        print()
    print()

def part_2(data):
    data = as_grid(data)
    scores = [[(10**20, (-1, -1)) for _ in l] for l in data]
    S = (len(data) - 2, 1)
    E = (1, len(data[0]) - 2)
    scores[S[0]][S[1]] = (0, (0, 0))
    scores = djikstra(S, (0, 1), data, scores, E)
    tiles = get_tiles(E, scores, set(), (0, 0), S)
    return len((tiles)) + 1

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
