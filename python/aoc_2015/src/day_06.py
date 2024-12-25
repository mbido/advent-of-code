import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 6

def part_1(data):
    grid = np.zeros((1000, 1000))
    for line in data.split("\n"):
        l = line.split(",")
        x1 = int(l[0].split(" ")[-1])
        y1 = int(l[1].split(" ")[0])
        x2 = int(l[1].split(" ")[-1])
        y2 = int(l[-1])
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):      
                if "turn on" in line:
                    grid[i, j] = 1
                elif "turn off" in line:
                    grid[i, j] = 0
                else:
                    grid[i, j] = 1 - grid[i, j]
    return int(np.sum(grid))

def part_2(data):
    grid = np.zeros((1000, 1000))
    for line in data.split("\n"):
        l = line.split(",")
        x1 = int(l[0].split(" ")[-1])
        y1 = int(l[1].split(" ")[0])
        x2 = int(l[1].split(" ")[-1])
        y2 = int(l[-1])
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):      
                if "turn on" in line:
                    grid[i, j] += 1
                elif "turn off" in line:
                    grid[i, j] = max(0, grid[i, j] - 1)
                else:
                    grid[i, j] += 2
    return int(np.sum(grid))

if __name__ == "__main__": 
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
