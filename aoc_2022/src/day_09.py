import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
import aoc_tools as aoct
from utils import *

YEAR = 2022
DAY = 9

data = aoct.get_input(YEAR, DAY)

res = 0

# graphs
# V = list(set(re.findall(r'[a-z]{2}', data)))
# V_T = {V[i] : i for i in range(len(V))}
# edges = [(V_T[a], V_T[b]) for a, b in re.findall(r'([a-z]{2})\-([a-z]{2})', data)]
# G = ig.Graph(edges=edges, directed=False)
# edges = [(V_T[a], V_T[b], int(c)) for a, b, c in re.findall(r'([a-z]{2})\-([a-z]{2})\-(\d+)', data)]
# G = ig.Graph(edges=[(s,t) for s,t,_ in edges], directed=False, edge_attrs={"weight": [w for _,_,w in edges]})


class Rope:
    def __init__(self):
        self.head_pos = [0, 0]
        self.tail_pos = [0, 0]
        self.tail_visited = {str(self.tail_pos)}

    def update_tail_pos(self):
        diff_x = self.tail_pos[0] - self.head_pos[0]
        diff_y = self.tail_pos[1] - self.head_pos[1]
        if abs(diff_x) > 1:
            self.tail_pos = self.head_pos.copy()
            self.tail_pos[0] += diff_x // abs(diff_x)
        elif abs(diff_y) > 1:
            self.tail_pos = self.head_pos.copy()
            self.tail_pos[1] += diff_y // abs(diff_y)
        self.tail_visited.add(str(self.tail_pos))

    def move_head(self, direct, times):
        directions = {"R": (1, 0), "U": (0, -1), "L": (-1, 0), "D": (0, 1)}
        d = directions[direct]
        for _ in range(times):
            self.head_pos[0] += d[0]
            self.head_pos[1] += d[1]
            self.update_tail_pos()


# data = as_grid(data)
rope = Rope()
for l in data.split("\n"):
    d, n = l.split(" ")
    rope.move_head(d, int(n))

print(len(rope.tail_visited))


class Rope2:
    def __init__(self, idx=0):
        self.head_pos = [0, 0]
        self.idx = idx
        self.tail = None if idx == 9 else Rope2(idx=idx + 1)
        self.tail_visited = set([str(self.tail.head_pos)]) if idx < 9 else set()

    def update_tail_pos(self):
        if self.tail is None:
            return

        changed = False

        # print(self.tail.idx, self.tail.head_pos)
        diff_x = self.tail.head_pos[0] - self.head_pos[0]
        diff_y = self.tail.head_pos[1] - self.head_pos[1]
        if abs(diff_x) > 1:
            self.tail.head_pos = self.head_pos.copy()
            self.tail.head_pos[0] += diff_x // abs(diff_x)
            changed = True
            # print(self.idx, self.tail.head_pos)
        elif abs(diff_y) > 1:
            self.tail.head_pos = self.head_pos.copy()
            self.tail.head_pos[1] += diff_y // abs(diff_y)
            changed = True
            # print(self.tail.idx, self.tail.head_pos)
        # print()
        if changed:
            self.tail.update_tail_pos()
            self.tail_visited.add(str(self.tail.head_pos))
            # print(
            #     f"Changed in {self.idx} on tail {self.tail.idx} new tail pos : {self.tail.head_pos}"
            # )

    def move_head(self, direct, times):
        directions = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}
        d = directions[direct]
        for _ in range(times):
            self.head_pos[0] += d[0]
            self.head_pos[1] += d[1]
            self.update_tail_pos()

    def get_tail_visited(self):
        if self.idx == 8:
            return self.tail_visited
        return self.tail.get_tail_visited()


data = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


rope = Rope2()
for l in data.split("\n"):
    d, n = l.split(" ")
    print()
    print(l)
    rope.move_head(d, int(n))

print(rope.get_tail_visited())
print(len(rope.get_tail_visited()))


def print_visited_grid(visited_set):
    if not visited_set:
        return

    # Parse coordinates from the set
    coords = []
    for s_coord in visited_set:
        # Remove brackets and split by comma
        s_coord = s_coord.strip("[]")
        x_str, y_str = s_coord.split(", ")
        coords.append((int(x_str), int(y_str)))

    min_x = min(c[0] for c in coords)
    max_x = max(c[0] for c in coords)
    min_y = min(c[1] for c in coords)
    max_y = max(c[1] for c in coords)

    # Create a grid representation
    # The y-coordinates usually increase downwards in grid printing, so we iterate from max_y down to min_y
    # The x-coordinates increase from left to right
    for y in range(max_y, min_y - 1, -1):
        row = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in coords:
                row += "#"
            else:
                row += "."
        print(row)


print_visited_grid(rope.get_tail_visited())
