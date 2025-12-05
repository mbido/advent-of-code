import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2017
DAY = 3


def part_1(data):
    x = int(data)
    k = int((math.sqrt(x) - 1) / 2) + 1
    n = (2 * k + 1) ** 2
    c = [n - i * 2 * k for i in range(4)]
    d = min([abs(a - x) for a in c])
    return 2 * k - d


def part_2(data):
    data = int(data)
    # data = 56
    grid = {(0, 0): 1}
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    di = 0
    coord = (0, 0)
    while grid[coord] <= data:
        while True:
            coord = (coord[0] + dirs[di][0], coord[1] + dirs[di][1])
            nw = [
                grid[key]
                for x, y in adj8
                if (key := (coord[0] + x, coord[1] + y)) in grid
            ]
            # print(coord, sum(nw), nw)
            snw = sum(nw)
            if snw > data:
                return snw
            grid[coord] = sum(nw)

            if (
                coord[0] + dirs[(di + 1) % 4][0],
                coord[1] + dirs[(di + 1) % 4][1],
            ) not in grid:
                break
        di = (di + 1) % 4

    return False


if __name__ == "__main__":
    data = aoct.get_input(YEAR, DAY)
    aoct.submit_answer(YEAR, DAY, part_1(data), send=False)
    aoct.submit_answer(YEAR, DAY, part_2(data), level=2, send=False)
