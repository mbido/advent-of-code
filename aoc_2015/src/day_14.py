import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..', '..')))
import aoc_tools as aoct
from utils import *

YEAR = 2015
DAY = 14

data = aoct.get_input(YEAR, DAY)
# print(data)
# data = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""

res = 0
deers  = []
#data = as_grid(data)
for l in data.split("\n"):
    deers.append(nums(l))

N = 2503

current = copy.deepcopy(deers)
dists = [0 for _ in deers]
for n in range(N):
    for i, d in enumerate(deers):
        cd = current[i]
        if cd[1] > 0:
            dists[i] += cd[0]
            current[i][1] -= 1
        elif cd[2] == 0:
            dists[i] += cd[0]
            current[i][1] = d[1] - 1
            current[i][2] = d[2]
        else:
            current[i][2] -= 1
print(max(dists))

# N = 1000

current = copy.deepcopy(deers)
dists = [0 for _ in deers]
points = [0 for _ in deers]
for n in range(N):
    for i, d in enumerate(deers):
        cd = current[i]
        if cd[1] > 0:
            dists[i] += cd[0]
            current[i][1] -= 1
        elif cd[2] == 0:
            dists[i] += cd[0]
            current[i][1] = d[1] - 1
            current[i][2] = d[2]
        else:
            current[i][2] -= 1

    m = max(dists)
    for i, d in enumerate(dists):
        if d == m:
            points[i] += 1
print(max(points))


# print(deers)
# print(res)
